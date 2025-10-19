import { useState, useEffect } from 'react';
import { suppliesService } from '../../services/suppliesService';
import { suppliersService } from '../../services/suppliersService';
import { useToast } from '../../hooks/useToast';
import SupplyCard from './SupplyCard';
import SupplyForm from './SupplyForm';

export default function SuppliesList() {
  const [supplies, setSupplies] = useState([]);
  const [suppliers, setSuppliers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const toast = useToast();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [suppliesData, suppliersData] = await Promise.all([
        suppliesService.getAll(),
        suppliersService.getAll()
      ]);
      setSupplies(suppliesData);
      setSuppliers(suppliersData);
    } catch (err) {
      toast.error('Не вдалося завантажити дані');
      console.error('Error loading data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цю поставку?')) {
      return;
    }

    try {
      await suppliesService.delete(id);
      toast.success('Поставку видалено');
      loadData();
    } catch (err) {
      toast.error('Не вдалося видалити поставку');
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      await suppliesService.create(data);
      toast.success('Поставку зареєстровано');
      setShowForm(false);
      loadData();
    } catch (err) {
      toast.error('Не вдалося зареєструвати поставку');
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
        <h2 className="text-2xl font-bold text-gray-900">Поставки</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Зареєструвати поставку
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <SupplyForm
            suppliers={suppliers}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {supplies.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає поставок</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {supplies.map((supply) => (
            <SupplyCard
              key={supply.id}
              supply={supply}
              suppliers={suppliers}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
