import { useState, useEffect } from 'react';

export default function StorekeeperForm({ storekeeper, warehouses, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    warehouse_id: ''
  });

  useEffect(() => {
    if (storekeeper) {
      setFormData({
        name: storekeeper.name,
        warehouse_id: storekeeper.warehouse_id
      });
    }
  }, [storekeeper]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'warehouse_id' ? parseInt(value) : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.name.trim()) {
      alert("Будь ласка, введіть ім'я комірника");
      return;
    }
    if (!formData.warehouse_id) {
      alert('Будь ласка, виберіть склад');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">
        {storekeeper ? 'Редагувати комірника' : 'Новий комірник'}
      </h3>

      <form onSubmit={handleSubmit}>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Ім'я <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="input-field"
              placeholder="Введіть ім'я комірника"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Склад <span className="text-red-500">*</span>
            </label>
            <select
              name="warehouse_id"
              value={formData.warehouse_id}
              onChange={handleChange}
              className="input-field"
              required
            >
              <option value="">Виберіть склад</option>
              {warehouses.map((warehouse) => (
                <option key={warehouse.id} value={warehouse.id}>
                  {warehouse.name} {warehouse.location && `(${warehouse.location})`}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            {storekeeper ? 'Зберегти' : 'Створити'}
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
