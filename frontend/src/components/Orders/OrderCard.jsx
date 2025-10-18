export default function OrderCard({ order, onDelete }) {
  const getStatusColor = (status) => {
    const colors = {
      pending: 'bg-yellow-100 text-yellow-800',
      confirmed: 'bg-blue-100 text-blue-800',
      delivered: 'bg-green-100 text-green-800',
      cancelled: 'bg-red-100 text-red-800',
    };
    return colors[status] || 'bg-gray-100 text-gray-800';
  };

  const getStatusText = (status) => {
    const texts = {
      pending: 'Очікує',
      confirmed: 'Підтверджено',
      delivered: 'Доставлено',
      cancelled: 'Скасовано',
    };
    return texts[status] || status;
  };

  return (
    <div className="card p-4">
      <div className="flex justify-between items-start mb-3">
        <div>
          <h3 className="text-lg font-semibold text-gray-900">
            Замовлення #{order.order_id || order.id}
          </h3>
          <p className="text-sm text-gray-600 mt-1">
            Постачальник: {order.supplier}
          </p>
        </div>
        <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(order.status)}`}>
          {getStatusText(order.status)}
        </span>
      </div>

      {order.date && (
        <p className="text-sm text-gray-500 mb-3">
          📅 {new Date(order.date).toLocaleDateString('uk-UA')}
        </p>
      )}

      <button
        onClick={() => onDelete(order.id)}
        className="w-full bg-red-50 text-red-700 hover:bg-red-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
      >
        Видалити
      </button>
    </div>
  );
}
