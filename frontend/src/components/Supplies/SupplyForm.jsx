import { useState } from 'react';

export default function SupplyForm({ suppliers, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    supplier_id: '',
    date: new Date().toISOString().split('T')[0]
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'supplier_id' ? parseInt(value) : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.supplier_id) {
      alert('Будь ласка, виберіть постачальника');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">Реєстрація нової поставки</h3>

      <form onSubmit={handleSubmit}>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Постачальник <span className="text-red-500">*</span>
            </label>
            <select
              name="supplier_id"
              value={formData.supplier_id}
              onChange={handleChange}
              className="input-field"
              required
            >
              <option value="">Виберіть постачальника</option>
              {suppliers.map((supplier) => (
                <option key={supplier.id} value={supplier.id}>
                  {supplier.name}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Дата поставки
            </label>
            <input
              type="date"
              name="date"
              value={formData.date}
              onChange={handleChange}
              className="input-field"
            />
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            Зареєструвати
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
