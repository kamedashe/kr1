# Frontend - React Application

## Технології

- **React 18** - UI бібліотека
- **Vite** - Build tool (швидкий dev server)
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Роутинг
- **Axios** - HTTP клієнт

## Встановлення

1. Встановіть залежності:
```bash
npm install
```

## Запуск

```bash
npm run dev
```

Додаток запуститься на `http://localhost:5173`

## Збірка для продакшену

```bash
npm run build
```

Скомпільовані файли будуть в папці `dist/`

## Структура проекту

```
src/
├── components/           # React компоненти
│   ├── Layout/          # Header, Sidebar, Layout
│   ├── Suppliers/       # Компоненти постачальників
│   ├── Components/      # Компоненти комплектуючих
│   └── Warehouses/      # Компоненти складів
├── pages/               # Сторінки
│   ├── Dashboard.jsx
│   ├── SuppliersPage.jsx
│   ├── ComponentsPage.jsx
│   └── WarehousesPage.jsx
├── services/            # API клієнти
│   ├── api.js
│   ├── suppliersService.js
│   ├── componentsService.js
│   └── warehousesService.js
├── App.jsx              # Головний компонент з роутами
├── main.jsx             # Entry point
└── index.css            # Глобальні стилі + Tailwind

```

## Автентифікація

За замовчуванням використовується Basic Auth:
- Username: `admin`
- Password: `admin`

Налаштовується в `src/services/api.js`

## API Endpoints

Frontend з'єднується з backend API на `http://localhost:8000/api/v1`

Можна змінити в `src/services/api.js`
