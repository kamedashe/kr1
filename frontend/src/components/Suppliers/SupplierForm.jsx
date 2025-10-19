import { useState, useEffect } from 'react';

export default function SupplierForm({ supplier, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    contact_info: ''
  });

  useEffect(() => {
    if (supplier) {
      setFormData({
        name: supplier.name,
        contact_info: supplier.contact_info || ''
      });
    }
  }, [supplier]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.name.trim()) {
      alert('Будь ласка, введіть назву постачальника');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">
        {supplier ? 'Редагувати постачальника' : 'Новий постачальник'}
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
              placeholder="Введіть назву постачальника"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Контактна інформація
            </label>
            <input
              type="text"
              name="contact_info"
              value={formData.contact_info}
              onChange={handleChange}
              className="input-field"
              placeholder="Телефон, email, адреса..."
            />
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            {supplier ? 'Зберегти' : 'Створити'}
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
