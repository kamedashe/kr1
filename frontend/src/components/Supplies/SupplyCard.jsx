export default function SupplyCard({ supply, suppliers, onDelete }) {
  const supplier = suppliers.find(s => s.id === supply.supplier_id);

  return (
    <div className="card p-4">
      <div className="flex justify-between items-start mb-3">
        <div>
          <h3 className="text-lg font-semibold text-gray-900">
            Поставка #{supply.id}
          </h3>
          <p className="text-sm text-gray-600 mt-1">
            🏢 {supplier ? supplier.name : 'Невідомий постачальник'}
          </p>
        </div>
      </div>

      {supply.date && (
        <p className="text-sm text-gray-500 mb-3">
          📅 {new Date(supply.date).toLocaleDateString('uk-UA')}
        </p>
      )}

      <button
        onClick={() => onDelete(supply.id)}
        className="w-full bg-red-50 text-red-700 hover:bg-red-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
      >
        Видалити
      </button>
    </div>
  );
}
