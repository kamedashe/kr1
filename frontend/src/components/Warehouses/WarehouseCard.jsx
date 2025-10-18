export default function WarehouseCard({ warehouse, onEdit, onDelete }) {
  return (
    <div className="card p-4">
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-lg font-semibold text-gray-900">{warehouse.name}</h3>
        <span className="text-xs text-gray-500">#{warehouse.id}</span>
      </div>

      <div className="mb-4">
        <p className="text-sm text-gray-600">
          📍 {warehouse.location || 'Локація не вказана'}
        </p>
      </div>

      <div className="flex space-x-2">
        <button
          onClick={() => onEdit(warehouse)}
          className="flex-1 bg-primary-50 text-primary-700 hover:bg-primary-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Редагувати
        </button>
        <button
          onClick={() => onDelete(warehouse.id)}
          className="flex-1 bg-red-50 text-red-700 hover:bg-red-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Видалити
        </button>
      </div>
    </div>
  );
}
