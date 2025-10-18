import { useState, useEffect } from 'react';
import { suppliersService } from '../../services/suppliersService';
import SupplierCard from './SupplierCard';
import SupplierForm from './SupplierForm';

export default function SuppliersList() {
  const [suppliers, setSuppliers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingSupplier, setEditingSupplier] = useState(null);

  useEffect(() => {
    loadSuppliers();
  }, []);

  const loadSuppliers = async () => {
    try {
      setLoading(true);
      const data = await suppliersService.getAll();
      setSuppliers(data);
      setError(null);
    } catch (err) {
      setError('Не вдалося завантажити постачальників');
      console.error('Error loading suppliers:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingSupplier(null);
    setShowForm(true);
  };

  const handleEdit = (supplier) => {
    setEditingSupplier(supplier);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цього постачальника?')) {
      return;
    }

    try {
      await suppliersService.delete(id);
      loadSuppliers();
    } catch (err) {
      alert('Не вдалося видалити постачальника');
      console.error('Error deleting supplier:', err);
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingSupplier) {
        await suppliersService.update(editingSupplier.id, data);
      } else {
        await suppliersService.create(data);
      }
      setShowForm(false);
      loadSuppliers();
    } catch (err) {
      alert('Не вдалося зберегти постачальника');
      console.error('Error saving supplier:', err);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-gray-600">Завантаження...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
        {error}
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-900">Постачальники</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Додати постачальника
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <SupplierForm
            supplier={editingSupplier}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {suppliers.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає постачальників</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {suppliers.map((supplier) => (
            <SupplierCard
              key={supplier.id}
              supplier={supplier}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
