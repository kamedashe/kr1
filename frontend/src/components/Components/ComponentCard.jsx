export default function ComponentCard({ component, onEdit, onDelete }) {
  const getStockStatus = (qty) => {
    if (qty === 0) return { color: 'text-red-600', label: 'Немає в наявності' };
    if (qty < 50) return { color: 'text-yellow-600', label: 'Низький запас' };
    return { color: 'text-green-600', label: 'В наявності' };
  };

  const status = getStockStatus(component.qty);

  return (
    <div className="card p-4">
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-lg font-semibold text-gray-900">{component.name}</h3>
        <span className="text-xs text-gray-500">#{component.id}</span>
      </div>

      <div className="mb-4 space-y-1">
        <p className="text-2xl font-bold text-primary-600">
          {component.qty} <span className="text-sm font-normal text-gray-500">{component.unit}</span>
        </p>
        <p className={`text-sm font-medium ${status.color}`}>
          {status.label}
        </p>
      </div>

      <div className="flex space-x-2">
        <button
          onClick={() => onEdit(component)}
          className="flex-1 bg-primary-50 text-primary-700 hover:bg-primary-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Редагувати
        </button>
        <button
          onClick={() => onDelete(component.id)}
          className="flex-1 bg-red-50 text-red-700 hover:bg-red-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Видалити
        </button>
      </div>
    </div>
  );
}
