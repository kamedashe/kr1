import { useState, useEffect } from 'react';

export default function ComponentForm({ component, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    unit: 'шт',
    qty: 0
  });

  useEffect(() => {
    if (component) {
      setFormData({
        name: component.name,
        unit: component.unit || 'шт',
        qty: component.qty || 0
      });
    }
  }, [component]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'qty' ? parseInt(value) || 0 : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.name.trim()) {
      alert('Будь ласка, введіть назву комплектуючого');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">
        {component ? 'Редагувати комплектуюче' : 'Нове комплектуюче'}
      </h3>

      <form onSubmit={handleSubmit}>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Назва <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="input-field"
              placeholder="Введіть назву комплектуючого"
              required
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Одиниця виміру
              </label>
              <select
                name="unit"
                value={formData.unit}
                onChange={handleChange}
                className="input-field"
              >
                <option value="шт">шт (штуки)</option>
                <option value="кг">кг (кілограми)</option>
                <option value="м">м (метри)</option>
                <option value="л">л (літри)</option>
                <option value="пач">пач (пачки)</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Кількість
              </label>
              <input
                type="number"
                name="qty"
                value={formData.qty}
                onChange={handleChange}
                className="input-field"
                min="0"
              />
            </div>
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            {component ? 'Зберегти' : 'Створити'}
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
