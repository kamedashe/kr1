import { NavLink } from 'react-router-dom';

const navigation = [
  { name: 'Дашборд', href: '/', icon: '📊' },
  { name: 'Постачальники', href: '/suppliers', icon: '🏢' },
  { name: 'Комплектуючі', href: '/components', icon: '🔧' },
  { name: 'Склади', href: '/warehouses', icon: '🏭' },
  { name: 'Замовлення', href: '/orders', icon: '📦' },
  { name: 'Комірники', href: '/storekeepers', icon: '👷' },
  { name: 'Поставки', href: '/supplies', icon: '🚚' },
];

export default function Sidebar() {
  return (
    <div className="hidden md:flex md:w-64 md:flex-col md:fixed md:inset-y-0 md:pt-16">
      <div className="flex-1 flex flex-col min-h-0 bg-gray-50 border-r border-gray-200">
        <div className="flex-1 flex flex-col pt-5 pb-4 overflow-y-auto">
          <nav className="mt-5 flex-1 px-2 space-y-1">
            {navigation.map((item) => (
              <NavLink
                key={item.name}
                to={item.href}
                className={({ isActive }) =>
                  `group flex items-center px-2 py-2 text-sm font-medium rounded-md transition-colors ${
                    isActive
                      ? 'bg-primary-100 text-primary-900'
                      : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
                  }`
                }
              >
                <span className="mr-3 text-xl">{item.icon}</span>
                {item.name}
              </NavLink>
            ))}
          </nav>
        </div>
      </div>
    </div>
  );
}
