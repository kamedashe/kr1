import { useState, useEffect } from 'react';
import { ordersService } from '../../services/ordersService';
import { useToast } from '../../hooks/useToast';
import OrderCard from './OrderCard';
import OrderForm from './OrderForm';

export default function OrdersList() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const toast = useToast();

  useEffect(() => {
    loadOrders();
  }, []);

  const loadOrders = async () => {
    try {
      setLoading(true);
      const data = await ordersService.getAll();
      setOrders(data);
    } catch (err) {
      toast.error('Не вдалося завантажити замовлення');
      console.error('Error loading orders:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити це замовлення?')) {
      return;
    }

    try {
      await ordersService.delete(id);
      toast.success('Замовлення видалено');
      loadOrders();
    } catch (err) {
      toast.error('Не вдалося видалити замовлення');
      console.error('Error deleting order:', err);
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      await ordersService.create(data);
      toast.success('Замовлення створено');
      setShowForm(false);
      loadOrders();
    } catch (err) {
      toast.error('Не вдалося створити замовлення');
      console.error('Error creating order:', err);
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
        <h2 className="text-2xl font-bold text-gray-900">Замовлення</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Створити замовлення
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <OrderForm
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {orders.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає замовлень</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {orders.map((order) => (
            <OrderCard
              key={order.id}
              order={order}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
