import { useState, useEffect } from 'react';
import { componentsService } from '../../services/componentsService';
import ComponentCard from './ComponentCard';
import ComponentForm from './ComponentForm';

export default function ComponentsList() {
  const [components, setComponents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingComponent, setEditingComponent] = useState(null);

  useEffect(() => {
    loadComponents();
  }, []);

  const loadComponents = async () => {
    try {
      setLoading(true);
      const data = await componentsService.getAll();
      setComponents(data);
      setError(null);
    } catch (err) {
      setError('Не вдалося завантажити комплектуючі');
      console.error('Error loading components:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingComponent(null);
    setShowForm(true);
  };

  const handleEdit = (component) => {
    setEditingComponent(component);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити це комплектуюче?')) {
      return;
    }

    try {
      await componentsService.delete(id);
      loadComponents();
    } catch (err) {
      alert('Не вдалося видалити комплектуюче');
      console.error('Error deleting component:', err);
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingComponent) {
        await componentsService.update(editingComponent.id, data);
      } else {
        await componentsService.create(data);
      }
      setShowForm(false);
      loadComponents();
    } catch (err) {
      alert('Не вдалося зберегти комплектуюче');
      console.error('Error saving component:', err);
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
        <h2 className="text-2xl font-bold text-gray-900">Комплектуючі</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Додати комплектуюче
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <ComponentForm
            component={editingComponent}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {components.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає комплектуючих</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {components.map((component) => (
            <ComponentCard
              key={component.id}
              component={component}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
