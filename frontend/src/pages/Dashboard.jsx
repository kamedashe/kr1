import { useState, useEffect } from 'react';
import { suppliersService } from '../services/suppliersService';
import { componentsService } from '../services/componentsService';
import { warehousesService } from '../services/warehousesService';
import { Link } from 'react-router-dom';

export default function Dashboard() {
  const [stats, setStats] = useState({
    suppliers: 0,
    components: 0,
    warehouses: 0,
    lowStock: 0
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const [suppliers, components, warehouses] = await Promise.all([
        suppliersService.getAll(),
        componentsService.getAll(),
        warehousesService.getAll()
      ]);

      const lowStock = components.filter(c => c.qty < 50).length;

      setStats({
        suppliers: suppliers.length,
        components: components.length,
        warehouses: warehouses.length,
        lowStock
      });
    } catch (err) {
      console.error('Error loading stats:', err);
    } finally {
      setLoading(false);
    }
  };

  const statCards = [
    { title: 'Постачальники', value: stats.suppliers, icon: '🏢', link: '/suppliers', color: 'bg-blue-500' },
    { title: 'Комплектуючі', value: stats.components, icon: '🔧', link: '/components', color: 'bg-green-500' },
    { title: 'Склади', value: stats.warehouses, icon: '🏭', link: '/warehouses', color: 'bg-purple-500' },
    { title: 'Низький запас', value: stats.lowStock, icon: '⚠️', link: '/components', color: 'bg-yellow-500' },
  ];

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-gray-600">Завантаження...</div>
      </div>
    );
  }

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Дашборд</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {statCards.map((stat) => (
          <Link
            key={stat.title}
            to={stat.link}
            className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-6"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">{stat.title}</p>
                <p className="text-3xl font-bold text-gray-900">{stat.value}</p>
              </div>
              <div className={`${stat.color} w-12 h-12 rounded-lg flex items-center justify-center text-2xl`}>
                {stat.icon}
              </div>
            </div>
          </Link>
        ))}
      </div>

      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold mb-4">Швидкі дії</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Link to="/suppliers" className="btn-primary text-center">
            Керувати постачальниками
          </Link>
          <Link to="/components" className="btn-primary text-center">
            Керувати комплектуючими
          </Link>
          <Link to="/warehouses" className="btn-primary text-center">
            Керувати складами
          </Link>
        </div>
      </div>
    </div>
  );
}
