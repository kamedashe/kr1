# План покращення веб-додатка

## ✅ Виконано

- [x] Видалено старі Tkinter файли (ui/, controllers/, main.py)
- [x] Видалено дублікати (models/, services/, dao/ з кореня)
- [x] Базова функціональність: Постачальники, Комплектуючі, Склади

---

## 🎯 Нові функції для додавання

### 1. Замовлення (Orders) 📦
**Backend:**
- API endpoints вже існують (OrderService, OrderDAO)
- Потрібно додати до FastAPI

**Frontend:**
- OrdersPage - сторінка зі списком замовлень
- OrderForm - форма створення/редагування
- OrderCard - картка замовлення з статусом

**Функції:**
- Створення замовлень постачальникам
- Статуси: pending, confirmed, delivered, cancelled
- Прив'язка до постачальників
- Історія замовлень

---

### 2. Комірники (Storekeepers) 👷
**Backend:**
- API endpoints (StorekeeperService, StorekeeperDAO існують)
- Додати до FastAPI

**Frontend:**
- StorekeepersPage
- StorekeeperForm
- StorekeeperCard

**Функції:**
- Управління комірниками
- Призначення до складів
- Контактна інформація

---

### 3. Поставки (Supplies/Deliveries) 🚚
**Backend:**
- API endpoints (SupplyService, SupplyDAO існують)
- Додати до FastAPI

**Frontend:**
- SuppliesPage
- SupplyForm - реєстрація нової поставки
- SupplyCard - деталі поставки

**Функції:**
- Реєстрація поставок
- Записи поставок (Supply Records)
- Зв'язок з постачальниками та комплектуючими
- Автоматичне оновлення залишків

---

### 4. Звіти (Reports) 📊
**Backend:**
- ReportService існує
- PDF/CSV export strategy patterns існують
- Додати API endpoints

**Frontend:**
- ReportsPage
- Різні типи звітів:
  - Залишки на складах
  - Історія замовлень
  - Рух комплектуючих
  - Статистика постачальників

**Функції:**
- Генерація звітів
- Експорт в PDF/CSV
- Фільтри по датах
- Візуалізація даних

---

## 🎨 UX Покращення

### 1. Toast Notifications 🔔
**Бібліотека:** react-hot-toast

**Замінити:**
- `alert()` → toast
- `confirm()` → toast з кнопками
- `messagebox` → красиві сповіщення

**Типи:**
- Success (зелений)
- Error (червоний)
- Warning (жовтий)
- Info (синій)

---

### 2. Пошук та Фільтрація 🔍
**Для всіх таблиць:**
- Search bar вгорі
- Реалтайм пошук
- Фільтри по колонках
- Збереження фільтрів

**Приклад:**
```jsx
<SearchBar
  placeholder="Шукати постачальника..."
  onSearch={handleSearch}
/>
<FilterPanel
  filters={['Всі', 'Активні', 'Заблоковані']}
  onFilter={handleFilter}
/>
```

---

### 3. Сортування 🔄
**Для всіх таблиць:**
- Клік по заголовку колонки
- Ascending/Descending
- Індикатор напрямку сортування (↑↓)
- Multiple column sort (Ctrl+click)

---

### 4. Пагінація 📄
**Для великих списків:**
- Items per page: 10, 25, 50, 100
- Навігація: ← 1 2 3 ... 10 →
- Go to page
- Total items count

---

## 📐 Архітектура рішення

### Shared Components
Створимо переповторюваний і компоненти:

```
frontend/src/components/
├── Common/
│   ├── Table.jsx           # Універсальна таблиця з пошуком/сортуванням/пагінацією
│   ├── SearchBar.jsx       # Пошукова панель
│   ├── Pagination.jsx      # Пагінація
│   ├── FilterPanel.jsx     # Панель фільтрів
│   ├── Modal.jsx           # Модальне вікно
│   └── Toast.jsx           # Toast wrapper
```

### Custom Hooks
```
frontend/src/hooks/
├── useTable.js         # Логіка таблиці (search, sort, pagination)
├── useToast.js         # Toast notifications
├── useModal.js         # Модальні вікна
└── useFetch.js         # Data fetching з кешуванням
```

---

## 🚀 План реалізації (порядок)

### Фаза 1: UX Foundation (1-2 год)
1. ✅ Додати react-hot-toast
2. ✅ Створити useToast hook
3. ✅ Замінити всі alert/confirm на toast
4. ✅ Створити універсальні компоненти (Table, SearchBar, Pagination)

### Фаза 2: Orders (2-3 год)
1. Backend API для Orders
2. Frontend OrdersPage
3. CRUD операції
4. Інтеграція з постачальниками

### Фаза 3: Storekeepers (1-2 год)
1. Backend API
2. Frontend StorekeepersPage
3. CRUD операції
4. Призначення до складів

### Фаза 4: Supplies (2-3 год)
1. Backend API
2. Frontend SuppliesPage
3. Реєстрація поставок
4. Автоматичне оновлення залишків

### Фаза 5: Reports (2-3 год)
1. Backend API з PDF/CSV export
2. Frontend ReportsPage
3. Різні типи звітів
4. Експорт функціональність

### Фаза 6: Polish (1 год)
1. Фінальне тестування
2. Виправлення багів
3. Оптимізація
4. Документація

---

## 📊 Очікуваний результат

**Повнофункціональний веб-додаток з:**
- ✅ Управління постачальниками
- ✅ Управління комплектуючими
- ✅ Управління складами
- ✅ Замовлення постачальникам
- ✅ Комірники та їх призначення
- ✅ Реєстрація поставок
- ✅ Звіти та експорт даних
- ✅ Пошук, сортування, пагінація
- ✅ Красиві toast notifications
- ✅ Респонсивний дизайн
- ✅ Сучасний UX/UI

**Час реалізації:** 8-12 годин

**Готово до продакшн!** 🎉

---

Почати з Фази 1?
