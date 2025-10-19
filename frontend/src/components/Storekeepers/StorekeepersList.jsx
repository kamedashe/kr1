import { useState, useEffect } from 'react';
import { storekeepersService } from '../../services/storekeepersService';
import { warehousesService } from '../../services/warehousesService';
import { useToast } from '../../hooks/useToast';
import StorekeeperCard from './StorekeeperCard';
import StorekeeperForm from './StorekeeperForm';

export default function StorekeepersList() {
  const [storekeepers, setStorekeepers] = useState([]);
  const [warehouses, setWarehouses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingStorekeeper, setEditingStorekeeper] = useState(null);
  const toast = useToast();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [storekeepersData, warehousesData] = await Promise.all([
        storekeepersService.getAll(),
        warehousesService.getAll()
      ]);
      setStorekeepers(storekeepersData);
      setWarehouses(warehousesData);
    } catch (err) {
      toast.error('Не вдалося завантажити дані');
      console.error('Error loading data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingStorekeeper(null);
    setShowForm(true);
  };

  const handleEdit = (storekeeper) => {
    setEditingStorekeeper(storekeeper);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цього комірника?')) {
      return;
    }

    try {
      await storekeepersService.delete(id);
      toast.success('Комірника видалено');
      loadData();
    } catch (err) {
      toast.error('Не вдалося видалити комірника');
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingStorekeeper) {
        await storekeepersService.update(editingStorekeeper.id, data);
        toast.success('Комірника оновлено');
      } else {
        await storekeepersService.create(data);
        toast.success('Комірника створено');
      }
      setShowForm(false);
      loadData();
    } catch (err) {
      toast.error('Не вдалося зберегти комірника');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-gray-600">Завантаження...</div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-900">Комірники</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Додати комірника
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <StorekeeperForm
            storekeeper={editingStorekeeper}
            warehouses={warehouses}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {storekeepers.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає комірників</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {storekeepers.map((storekeeper) => (
            <StorekeeperCard
              key={storekeeper.id}
              storekeeper={storekeeper}
              warehouses={warehouses}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
