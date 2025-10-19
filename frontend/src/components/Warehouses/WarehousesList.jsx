import { useState, useEffect } from 'react';
import { warehousesService } from '../../services/warehousesService';
import WarehouseCard from './WarehouseCard';
import WarehouseForm from './WarehouseForm';

export default function WarehousesList() {
  const [warehouses, setWarehouses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingWarehouse, setEditingWarehouse] = useState(null);

  useEffect(() => {
    loadWarehouses();
  }, []);

  const loadWarehouses = async () => {
    try {
      setLoading(true);
      const data = await warehousesService.getAll();
      setWarehouses(data);
      setError(null);
    } catch (err) {
      setError('Не вдалося завантажити склади');
      console.error('Error loading warehouses:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingWarehouse(null);
    setShowForm(true);
  };

  const handleEdit = (warehouse) => {
    setEditingWarehouse(warehouse);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цей склад?')) {
      return;
    }

    try {
      await warehousesService.delete(id);
      loadWarehouses();
    } catch (err) {
      alert('Не вдалося видалити склад');
      console.error('Error deleting warehouse:', err);
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingWarehouse) {
        await warehousesService.update(editingWarehouse.id, data);
      } else {
        await warehousesService.create(data);
      }
      setShowForm(false);
      loadWarehouses();
    } catch (err) {
      alert('Не вдалося зберегти склад');
      console.error('Error saving warehouse:', err);
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
        <h2 className="text-2xl font-bold text-gray-900">Склади</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Додати склад
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <WarehouseForm
            warehouse={editingWarehouse}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {warehouses.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає складів</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {warehouses.map((warehouse) => (
            <WarehouseCard
              key={warehouse.id}
              warehouse={warehouse}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
