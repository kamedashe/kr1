# Лістинг коду проекту КР1

## Структура проекту

Веб-додаток для управління поставками комплектуючих
- **Backend**: FastAPI + SQLite
- **Frontend**: React + Vite + Tailwind CSS

## Зміст

- [Documentation](#documentation) (8 файлів)
- [Root](#root) (3 файлів)
- [Backend - Config](#backend-config) (7 файлів)
- [Backend - Core](#backend-core) (4 файлів)
- [Backend - Database](#backend-database) (4 файлів)
- [Backend - Models](#backend-models) (8 файлів)
- [Backend - DAO](#backend-dao) (11 файлів)
- [Backend - Services](#backend-services) (13 файлів)
- [Backend - API](#backend-api) (7 файлів)
- [Frontend - Config](#frontend-config) (9 файлів)
- [Frontend - Services](#frontend-services) (6 файлів)
- [Frontend - Hooks](#frontend-hooks) (1 файлів)
- [Frontend - Pages](#frontend-pages) (7 файлів)
- [Frontend - Components](#frontend-components) (22 файлів)
- [Tests](#tests) (21 файлів)

---

## Documentation

### `CLEANUP_PLAN.md`

```markdown
# План очищення проекту

## 📦 Файли/папки ДЛЯ ВИДАЛЕННЯ (старий Tkinter код)

### UI (Tkinter - більше не потрібен)
- [ ] `ui/` - весь каталог з Tkinter інтерфейсом
  - component_tab.py
  - main_window.py
  - orders_tab.py
  - reports_tab.py
  - storekeeper_tab.py
  - supplier_tab.py
  - supplier_window.py
  - suppliers_tab.py
  - supply_tab.py
  - warehouse_tab.py
  - warehouse_window.py

### Controllers (старі - тепер в backend/app/api/)
- [ ] `controllers/` - весь каталог
  - component_controller.py
  - orders_controller.py
  - report_controller.py
  - storekeeper_controller.py
  - supplier_controller.py
  - supply_controller.py
  - warehouse_controller.py

### Старі модулі в корені (дублікати - тепер в backend/app/)
- [ ] `models/` - перенесено в backend/app/models/
- [ ] `services/` - перенесено в backend/app/services/
- [ ] `dao/` - перенесено в backend/app/dao/

### Інші старі файли
- [ ] `main.py` - старий Tkinter entry point
- [ ] `logging_config.py` - якщо не використовується
- [ ] `contextcodex.md` - схоже видалено
- [ ] `code_listing.md` - застарілий лістинг

### Builder/Strategy (якщо не використовуються в API)
- [ ] `builder/` - перевірити чи використовується
- [ ] `strategy/` - перевірити чи використовується

### Тести старого коду
- [ ] `tests/controller/` - тести старих контролерів
- [ ] `tests/service/` - можливо залишити
- [ ] `tests/dao/` - можливо залишити

---

## ✅ Файли/папки ДЛЯ ЗБЕРЕЖЕННЯ

### Новий веб-додаток
- ✅ `backend/` - FastAPI backend
- ✅ `frontend/` - React frontend
- ✅ `db/` - база даних (спільна)

### Документація
- ✅ `README_WEB.md` - головна документація
- ✅ `QUICK_START.md` - швидкий старт
- ✅ `WEB_MIGRATION_GUIDE.md` - посібник з міграції
- ✅ `.claude/` - Claude Code конфігурація
- ✅ `specs/` - специфікації (якщо є)

### Git
- ✅ `.git/`
- ✅ `.gitignore`

---

## 🎯 Рекомендації

1. **Створити архів старого коду** перед видаленням (на всяк випадок)
2. **Видалити старі файли** поетапно
3. **Перевірити чи все працює** після кожного видалення
4. **Оновити .gitignore** для нової структури

---

## 📊 Нова структура проекту (після очищення)

```
kr1/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── core/        # Config, auth
│   │   ├── models/      # Data models
│   │   ├── services/    # Business logic
│   │   ├── dao/         # Database access
│   │   ├── db/          # Database
│   │   └── main.py
│   ├── venv/
│   ├── requirements.txt
│   └── run.py
│
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── ...
│   ├── node_modules/
│   ├── package.json
│   └── ...
│
├── db/                  # Спільна база даних
│   └── supply.db
│
├── .claude/             # Claude Code config
├── specs/               # Документація
├── README_WEB.md
├── QUICK_START.md
└── WEB_MIGRATION_GUIDE.md
```

Набагато чистіше! 🎉
```

### `ENHANCEMENT_PLAN.md`

```markdown
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
```

### `FEATURES_COMPLETED.md`

```markdown
# ✅ Нові функції додано!

## 🎉 Що нового

### Backend API (FastAPI) - 3 нових модулі

#### 1. Orders API (`/api/v1/orders/`)
- ✅ `GET /orders/` - Список всіх замовлень
- ✅ `POST /orders/` - Створення замовлення
- ✅ `DELETE /orders/{id}` - Видалення замовлення

**Файл:** `backend/app/api/orders.py`

#### 2. Storekeepers API (`/api/v1/storekeepers/`)
- ✅ `GET /storekeepers/` - Список комірників
- ✅ `GET /storekeepers/{id}` - Комірник за ID
- ✅ `POST /storekeepers/` - Створення комірника
- ✅ `PUT /storekeepers/{id}` - Оновлення комірника
- ✅ `DELETE /storekeepers/{id}` - Видалення комірника

**Файл:** `backend/app/api/storekeepers.py`

#### 3. Supplies API (`/api/v1/supplies/`)
- ✅ `GET /supplies/` - Список поставок
- ✅ `POST /supplies/` - Реєстрація поставки
- ✅ `DELETE /supplies/{id}` - Видалення поставки

**Файл:** `backend/app/api/supplies.py`

---

### Frontend (React) - 3 нових сторінки

#### 1. Замовлення 📦
**Компоненти:**
- `OrdersList.jsx` - Список з CRUD операціями
- `OrderCard.jsx` - Картка замовлення зі статусами
- `OrderForm.jsx` - Форма створення

**Функції:**
- Створення замовлень постачальникам
- Статуси: Очікує, Підтверджено, Доставлено, Скасовано
- Відображення дати
- Toast notifications

**Роут:** `/orders`

---

#### 2. Комірники 👷
**Компоненти:**
- `StorekeepersList.jsx` - Список з CRUD операціями
- `StorekeeperCard.jsx` - Картка з призначенням складу
- `StorekeeperForm.jsx` - Форма з вибором складу

**Функції:**
- Управління комірниками
- Призначення до складів
- Відображення локації складу
- Toast notifications

**Роут:** `/storekeepers`

---

#### 3. Поставки 🚚
**Компоненти:**
- `SuppliesList.jsx` - Список з CRUD операціями
- `SupplyCard.jsx` - Картка поставки
- `SupplyForm.jsx` - Форма реєстрації

**Функції:**
- Реєстрація поставок
- Зв'язок з постачальниками
- Відображення дати
- Toast notifications

**Роут:** `/supplies`

---

### Навігація оновлена 🧭

**Sidebar тепер містить:**
1. 📊 Дашборд
2. 🏢 Постачальники
3. 🔧 Комплектуючі
4. 🏭 Склади
5. 📦 **Замовлення** (НОВИЙ!)
6. 👷 **Комірники** (НОВИЙ!)
7. 🚚 **Поставки** (НОВИЙ!)

---

### API Services (Frontend)

**Нові сервіси:**
- `ordersService.js` - API клієнт для замовлень
- `storekeepersService.js` - API клієнт для комірників
- `suppliesService.js` - API клієнт для поставок

---

## 🎨 UX Покращення

### Toast Notifications ✅
- ✅ Додано `react-hot-toast`
- ✅ Створено `useToast` hook
- ✅ Замінено всі `alert()` на красиві toast
- ✅ Success/Error статуси з кольорами

**Використання в компонентах:**
```javascript
const toast = useToast();

// Success
toast.success('Замовлення створено');

// Error
toast.error('Не вдалося завантажити дані');
```

---

## 📊 Структура проекту (оновлена)

```
backend/app/api/
├── suppliers.py        ✅
├── components.py       ✅
├── warehouses.py       ✅
├── orders.py           ✅ НОВИЙ
├── storekeepers.py     ✅ НОВИЙ
└── supplies.py         ✅ НОВИЙ

frontend/src/
├── components/
│   ├── Orders/         ✅ НОВИЙ
│   ├── Storekeepers/   ✅ НОВИЙ
│   └── Supplies/       ✅ НОВИЙ
├── pages/
│   ├── OrdersPage.jsx      ✅ НОВИЙ
│   ├── StorekeepersPage.jsx ✅ НОВИЙ
│   └── SuppliesPage.jsx     ✅ НОВИЙ
├── services/
│   ├── ordersService.js        ✅ НОВИЙ
│   ├── storekeepersService.js  ✅ НОВИЙ
│   └── suppliesService.js      ✅ НОВИЙ
└── hooks/
    └── useToast.js     ✅ НОВИЙ
```

---

## 🚀 Як перевірити

### 1. Перезапустити Backend
```bash
cd backend
python run.py
```

### 2. Перезапустити Frontend
```bash
cd frontend
npm run dev
```

### 3. Протестувати нові модулі
- Відкрити http://localhost:5173
- Перейти на "Замовлення" в sidebar
- Створити нове замовлення
- Побачити toast notification!
- Те саме для Комірників та Поставок

---

## 📈 Прогрес

| Модуль | Backend | Frontend | Toast | Статус |
|--------|---------|----------|-------|--------|
| Постачальники | ✅ | ✅ | ✅ | Готово |
| Комплектуючі | ✅ | ✅ | ✅ | Готово |
| Склади | ✅ | ✅ | ✅ | Готово |
| Замовлення | ✅ | ✅ | ✅ | **НОВИЙ!** |
| Комірники | ✅ | ✅ | ✅ | **НОВИЙ!** |
| Поставки | ✅ | ✅ | ✅ | **НОВИЙ!** |
| Звіти | ⏳ | ⏳ | - | Наступний |

✅ - Готово | ⏳ - В планах | ❌ - Не почато

---

## 🎯 Наступні кроки (опціонально)

1. **Звіти та експорт** 📊
   - Генерація звітів
   - Експорт в PDF/CSV
   - Фільтри по датах

2. **Пошук та фільтрація** 🔍
   - Search bar для всіх таблиць
   - Фільтри по колонках
   - Збереження фільтрів

3. **Сортування** 🔄
   - Клік по заголовку = сортування
   - Ascending/Descending
   - Multiple column sort

4. **Пагінація** 📄
   - Items per page
   - Навігація по сторінках
   - Go to page

---

## 🎉 Готово!

**Тепер у вас повнофункціональний веб-додаток з 6 модулями!**

Перезапустіть обидва сервери і протестуйте нові функції! 🚀
```

### `PROGRESS_SUMMARY.md`

```markdown
# Підсумок прогресу міграції на веб

## ✅ Виконано

### 1. Очищення проекту
- ✅ Видалено старі Tkinter файли (ui/, controllers/)
- ✅ Видалено main.py (старий entry point)
- ✅ Видалено дублікати models/, services/, dao/ з кореня
- ✅ Видалено builder/, strategy/ (застарілі патерни)

### 2. Backend (FastAPI) - ГОТОВИЙ
```
backend/
├── app/
│   ├── api/
│   │   ├── suppliers.py      ✅ CRUD API
│   │   ├── components.py     ✅ CRUD API
│   │   └── warehouses.py     ✅ CRUD API
│   ├── core/
│   │   ├── config.py         ✅
│   │   └── auth.py           ✅ Basic Auth
│   ├── models/               ✅ Всі моделі
│   ├── services/             ✅ Вся бізнес-логіка
│   ├── dao/                  ✅ Database access
│   └── main.py               ✅ FastAPI app
```

### 3. Frontend (React) - БАЗОВА ВЕРСІЯ ГОТОВА
```
frontend/
├── src/
│   ├── components/
│   │   ├── Layout/           ✅ Header, Sidebar, Layout
│   │   ├── Suppliers/        ✅ SuppliersList, Form, Card
│   │   ├── Components/       ✅ ComponentsList, Form, Card
│   │   └── Warehouses/       ✅ WarehousesList, Form, Card
│   ├── pages/
│   │   ├── Dashboard.jsx     ✅ Статистика
│   │   ├── SuppliersPage     ✅
│   │   ├── ComponentsPage    ✅
│   │   └── WarehousesPage    ✅
│   ├── services/             ✅ API клієнти
│   ├── hooks/
│   │   └── useToast.js       ✅ НОВИЙ!
│   └── App.jsx               ✅ + Toaster
```

### 4. Toast Notifications - ДОДАНО
- ✅ Додано react-hot-toast в package.json
- ✅ Створено useToast hook
- ✅ Додано Toaster в App.jsx

---

## 🚀 Наступні кроки

### Завершити Фазу 1 (UX Foundation)
1. **Встановити залежності:**
   ```bash
   cd frontend
   npm install
   ```

2. **Оновити компоненти на використання toast:**
   - SuppliersList.jsx
   - ComponentsList.jsx
   - WarehousesList.jsx
   Замінити всі `alert()` та `window.confirm()` на toast

3. **Створити універсальні компоненти:**
   - SearchBar.jsx
   - Pagination.jsx
   - Table.jsx (з пошуком, сортуванням, пагінацією)

### Фаза 2-5 (Нові модулі)
Див. детальний план в **ENHANCEMENT_PLAN.md**

---

## 📝 Швидкий старт

### Backend (Terminal 1):
```bash
cd backend
venv\Scripts\activate
python run.py
```
✅ http://localhost:8000/docs

### Frontend (Terminal 2):
```bash
cd frontend
npm install
npm run dev
```
✅ http://localhost:5173

### Логін:
- admin / admin

---

## 📊 Статус

| Модуль | Backend API | Frontend | UX | Статус |
|--------|------------|----------|-----|---------|
| Постачальники | ✅ | ✅ | 🔄 | Працює |
| Комплектуючі | ✅ | ✅ | 🔄 | Працює |
| Склади | ✅ | ✅ | 🔄 | Працює |
| Замовлення | 🔄 | ❌ | ❌ | Треба додати |
| Комірники | 🔄 | ❌ | ❌ | Треба додати |
| Поставки | 🔄 | ❌ | ❌ | Треба додати |
| Звіти | 🔄 | ❌ | ❌ | Треба додати |

🔄 - В процесі | ✅ - Готово | ❌ - Треба зробити

---

## 🎯 Що далі?

1. **Запустіть проект** (backend + frontend)
2. **Встановіть npm install** в frontend
3. **Протестуйте базову функціональність**
4. Я продовжу додавати нові модулі згідно з планом

**Готово до продовження!** 🚀
```

### `QUICK_START.md`

```markdown
# 🚀 Швидкий старт веб-додатка

## Крок 1: Запустити Backend (Terminal 1)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

✅ Backend: http://localhost:8000
📚 API Docs: http://localhost:8000/docs

---

## Крок 2: Запустити Frontend (Terminal 2)

```bash
cd frontend
npm install
npm run dev
```

✅ Frontend: http://localhost:5173

---

## Крок 3: Відкрити додаток

1. Відкрийте браузер
2. Перейдіть на http://localhost:5173
3. Логін: `admin` / `admin`

---

## 🎉 Готово!

Тепер ви можете:
- ✅ Управляти постачальниками
- ✅ Керувати комплектуючими
- ✅ Додавати склади
- ✅ Переглядати статистику

---

## 📸 Скріншоти функціональності

### Дашборд
- Статистика по всіх модулях
- Швидкі посилання
- Попередження про низькі запаси

### Постачальники
- Список всіх постачальників
- Додавання/редагування
- Контактна інформація

### Комплектуючі
- Відстеження кількості
- Одиниці виміру
- Індикатори запасів

### Склади
- Управління складами
- Локації
- Залишки товарів

---

## 🔐 Користувачі для тестування

| Username | Password | Доступ |
|----------|----------|--------|
| admin    | admin    | Повний |
| user     | user     | Повний |

---

## 💡 Поради

1. **Завжди запускайте backend ПЕРЕД frontend**
2. **Використовуйте 2 термінали** - один для backend, інший для frontend
3. **Перевіряйте порти** - backend: 8000, frontend: 5173
4. **API документація** - http://localhost:8000/docs (дуже корисно!)

---

Детальна документація: [README_WEB.md](README_WEB.md)
```

### `README.md`

```markdown
# Інформаційна система для відділу комплектації підприємства

## Опис
Ця система дозволяє керувати постачальниками, складами, поставками, комплектуючими, контрактами та історією операцій. Реалізовано CRUD-операції, формування звітів (PDF/CSV), та перевірку відповідності контрактів.

Проєкт побудовано на Python із застосуванням шаблонів проектування:  
- **DAO** (Data Access Object)  
- **Facade**  
- **Builder**  
- **Strategy**  
- **Observer**

## Структура проєкту

├── builder/ # Патерн Builder (OrderBuilder)
├── dao/ # Data Access Object класи (SupplyDAO, SupplierDAO, ...)
├── models/ # Моделі предметної області
├── observer/ # Observer для автоматичних оновлень
├── services/ # Фасад-сервіси, бізнес-логіка
├── strategy/ # Експорт/звітність (PDFExportStrategy, CSVExportStrategy)
├── tests/ # Юніт-тести, чек-аркуші
├── ui/ # Tkinter GUI
├── main.py # Точка входу (main menu/інтерфейс)
└── README.md # Інструкція (цей файл)


## Встановлення залежностей

Переконайтесь, що у вас встановлений Python 3.10+  
Усі залежності — у `requirements.txt`.

```sh
pip install -r requirements.txt
Мінімальний набір:

pytest

fpdf

PyPDF2

Запуск програми

python main.py
За потреби змініть конфігурацію БД або шлях до файлів у налаштуваннях.

Запуск тестів

pytest
або для окремого модуля:


pytest tests/dao/
pytest tests/service/
Експорт та тест-кейси
Таблиця тест-кейсів знаходиться у файлі test_cases.csv або у додатку до пояснювальної записки.

Розширені приклади юніт-тестів — у теці tests/

Основні можливості
Керування постачальниками, комплектуючими, складами, поставками

Формування та експорт звітів у PDF і CSV

Перевірка та валідація контрактів

Підтримка багаторівневих сервісів і шаблонів проектування

Простий графічний інтерфейс на Tkinter

Покриття коду юніт-тестами

Автор
Курсова робота
Бецьков Б.І., група АС-232
2025 рік

```

### `README_WEB.md`

```markdown
# ІС відділу комплектації підприємства (Web версія)

**Сучасний веб-додаток для управління постачальниками, комплектуючими та складами**

## 🚀 Технології

### Backend
- **FastAPI** - Сучасний, швидкий веб-фреймворк
- **SQLite** - База даних
- **Pydantic** - Валідація даних
- **Uvicorn** - ASGI сервер

### Frontend
- **React 18** - UI бібліотека
- **Vite** - Build tool
- **Tailwind CSS** - CSS framework
- **React Router** - Роутинг
- **Axios** - HTTP клієнт

## 📁 Структура проекту

```
kr1/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── core/        # Config, auth
│   │   ├── models/      # Data models
│   │   ├── services/    # Business logic
│   │   ├── dao/         # Database access
│   │   └── main.py      # FastAPI app
│   ├── requirements.txt
│   └── run.py
│
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/  # React компоненти
│   │   ├── pages/       # Сторінки
│   │   ├── services/    # API клієнт
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── db/                  # База даних (спільна)
    └── supply.db
```

## ⚡ Швидкий старт

### 1. Запуск Backend

```bash
# Перейти в папку backend
cd backend

# Створити віртуальне середовище
python -m venv venv

# Активувати (Windows)
venv\Scripts\activate

# Встановити залежності
pip install -r requirements.txt

# Запустити сервер
python run.py
```

✅ Backend запуститься на **http://localhost:8000**

📚 API документація: **http://localhost:8000/docs**

### 2. Запуск Frontend

Відкрийте **НОВИЙ** термінал:

```bash
# Перейти в папку frontend
cd frontend

# Встановити залежності
npm install

# Запустити dev server
npm run dev
```

✅ Frontend запуститься на **http://localhost:5173**

### 3. Відкрити додаток

Відкрийте браузер та перейдіть на **http://localhost:5173**

**Логін:**
- Username: `admin`
- Password: `admin`

---

## 🎯 Функціональність

### ✨ Постачальники
- Перегляд списку постачальників
- Додавання нових постачальників
- Редагування інформації
- Видалення постачальників
- Пошук та фільтрація

### 🔧 Комплектуючі
- Управління комплектуючими
- Відстеження кількості
- Індикатори низьких запасів
- Різні одиниці виміру

### 🏭 Склади
- Управління складами
- Локації та адреси
- Перегляд залишків

### 📊 Дашборд
- Статистика в реальному часі
- Швидкі посилання
- Попередження про низькі запаси

---

## 🎨 UI/UX Особливості

- ✅ **Респонсивний дизайн** - працює на всіх пристроях
- ✅ **Сучасний інтерфейс** - Tailwind CSS
- ✅ **Швидкий та інтуїтивний** - React
- ✅ **Інтерактивні форми** - валідація в реальному часі
- ✅ **Візуальний фідбек** - індикатори завантаження, статуси

---

## 📖 Детальна документація

- [Backend README](backend/README.md) - Детальна інформація про backend
- [Frontend README](frontend/README.md) - Детальна інформація про frontend
- [API Documentation](http://localhost:8000/docs) - Swagger UI (після запуску backend)

---

## 🔐 Автентифікація

Базова HTTP автентифікація:

| Username | Password | Role |
|----------|----------|------|
| admin    | admin    | Admin|
| user     | user     | User |

Налаштовується в `backend/app/core/auth.py`

---

## 🛠️ Розробка

### Backend Development

```bash
cd backend

# Активувати venv
venv\Scripts\activate

# Запустити з auto-reload
python run.py
```

### Frontend Development

```bash
cd frontend

# Запустити dev server
npm run dev

# Build для продакшену
npm run build

# Preview production build
npm run preview
```

---

## 📝 API Endpoints

### Suppliers (Постачальники)
- `GET /api/v1/suppliers/` - Всі постачальники
- `POST /api/v1/suppliers/` - Створити
- `GET /api/v1/suppliers/{id}` - Отримати за ID
- `PUT /api/v1/suppliers/{id}` - Оновити
- `DELETE /api/v1/suppliers/{id}` - Видалити

### Components (Комплектуючі)
- `GET /api/v1/components/` - Всі комплектуючі
- `POST /api/v1/components/` - Створити
- `GET /api/v1/components/{id}` - Отримати за ID
- `PUT /api/v1/components/{id}` - Оновити
- `DELETE /api/v1/components/{id}` - Видалити

### Warehouses (Склади)
- `GET /api/v1/warehouses/` - Всі склади
- `GET /api/v1/warehouses/stock-levels` - Залишки
- `POST /api/v1/warehouses/` - Створити
- `GET /api/v1/warehouses/{id}` - Отримати за ID
- `PUT /api/v1/warehouses/{id}` - Оновити
- `DELETE /api/v1/warehouses/{id}` - Видалити

---

## 🐛 Troubleshooting

### Backend не запускається
```bash
# Перевірте, чи активовано venv
venv\Scripts\activate

# Переконайтеся, що залежності встановлені
pip install -r requirements.txt

# Перевірте порт 8000
netstat -an | findstr :8000
```

### Frontend не запускається
```bash
# Видаліть node_modules та package-lock.json
rm -rf node_modules package-lock.json

# Встановіть знову
npm install

# Спробуйте інший порт
npm run dev -- --port 3000
```

### CORS помилки
Переконайтеся, що backend запущений на порту 8000, а frontend на 5173. CORS налаштовано в `backend/app/core/config.py`.

---

## 📄 Ліцензія

Навчальний проект - Бецьков Б.І., група АС-232, 2025

---

## ⭐ Додаткові можливості для розвитку

- [ ] JWT автентифікація замість Basic Auth
- [ ] Реєстрація нових користувачів
- [ ] Система ролей та прав доступу
- [ ] Пошук та фільтрація
- [ ] Експорт даних (CSV, PDF)
- [ ] Графіки та аналітика
- [ ] Email сповіщення
- [ ] Історія змін
- [ ] API для мобільних додатків

---

**Успішної роботи! 🚀**
```

### `WEB_MIGRATION_GUIDE.md`

```markdown
# Посібник з міграції на веб-інтерфейс

## ✓ Що вже зроблено

### Backend (FastAPI) - ГОТОВО

Створена повноцінна backend архітектура:

```
backend/
├── app/
│   ├── api/                    # ✓ API endpoints
│   │   ├── suppliers.py       # ✓ CRUD для постачальників
│   │   ├── components.py      # ✓ CRUD для комплектуючих
│   │   └── warehouses.py      # ✓ CRUD для складів
│   ├── core/                   # ✓ Конфігурація та автентифікація
│   │   ├── config.py          # ✓ Налаштування додатка
│   │   └── auth.py            # ✓ Базова HTTP автентифікація
│   ├── models/                 # ✓ Моделі (скопійовані з проекту)
│   ├── services/               # ✓ Сервіси (скопійовані з проекту)
│   ├── dao/                    # ✓ DAO (скопійовані з проекту)
│   ├── db/                     # ✓ База даних
│   └── main.py                 # ✓ Головний FastAPI додаток
├── requirements.txt            # ✓ Залежності Python
├── run.py                      # ✓ Скрипт запуску
└── README.md                   # ✓ Документація
```

### Особливості:
- ✓ RESTful API для всіх операцій
- ✓ Автоматична документація (Swagger/ReDoc)
- ✓ Базова автентифікація (admin/admin, user/user)
- ✓ CORS налаштування для React
- ✓ Використання існуючої бізнес-логіки

---

## 📋 Наступні кроки

### 1. Запуск Backend

```bash
cd backend

# Створити віртуальне середовище
python -m venv venv

# Активувати (Windows)
venv\Scripts\activate

# Встановити залежності
pip install -r requirements.txt

# Запустити сервер
python run.py
```

**Перевірка**: Відкрийте http://localhost:8000/docs - побачите Swagger UI з API документацією

### 2. Створення Frontend (React + Tailwind CSS)

**Опція A: Використати Vite (рекомендовано)**

```bash
# В корені проекту
npm create vite@latest frontend -- --template react
cd frontend
npm install

# Встановити Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Встановити додаткові пакети
npm install axios react-router-dom
```

**Опція B: Використати Create React App**

```bash
npx create-react-app frontend
cd frontend
npm install axios react-router-dom tailwindcss
```

### 3. Налаштування Tailwind CSS

**tailwind.config.js:**
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

**src/index.css:**
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 4. Структура Frontend (рекомендована)

```
frontend/src/
├── components/          # React компоненти
│   ├── Layout/
│   │   ├── Header.jsx
│   │   ├── Sidebar.jsx
│   │   └── Footer.jsx
│   ├── Suppliers/
│   │   ├── SuppliersList.jsx
│   │   ├── SupplierForm.jsx
│   │   └── SupplierCard.jsx
│   ├── Components/
│   │   ├── ComponentsList.jsx
│   │   └── ComponentForm.jsx
│   └── Warehouses/
│       ├── WarehousesList.jsx
│       └── WarehouseForm.jsx
├── pages/               # Сторінки
│   ├── Dashboard.jsx
│   ├── SuppliersPage.jsx
│   ├── ComponentsPage.jsx
│   └── WarehousesPage.jsx
├── services/            # API клієнт
│   ├── api.js          # Axios конфігурація
│   ├── suppliersService.js
│   ├── componentsService.js
│   └── warehousesService.js
├── hooks/               # Custom hooks
│   └── useAuth.js
├── App.jsx              # Головний компонент
└── main.jsx             # Entry point
```

---

## 🎨 Приклад коду для Frontend

### services/api.js
```javascript
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  auth: {
    username: 'admin',
    password: 'admin'
  }
});

export default api;
```

### services/suppliersService.js
```javascript
import api from './api';

export const suppliersService = {
  getAll: () => api.get('/suppliers/'),
  getById: (id) => api.get(`/suppliers/${id}`),
  create: (data) => api.post('/suppliers/', data),
  update: (id, data) => api.put(`/suppliers/${id}`, data),
  delete: (id) => api.delete(`/suppliers/${id}`)
};
```

### components/Suppliers/SuppliersList.jsx
```javascript
import { useState, useEffect } from 'react';
import { suppliersService } from '../../services/suppliersService';

export default function SuppliersList() {
  const [suppliers, setSuppliers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadSuppliers();
  }, []);

  const loadSuppliers = async () => {
    try {
      const response = await suppliersService.getAll();
      setSuppliers(response.data);
    } catch (error) {
      console.error('Error loading suppliers:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="text-center p-4">Завантаження...</div>;

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Постачальники</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {suppliers.map(supplier => (
          <div key={supplier.id} className="bg-white shadow-md rounded-lg p-4">
            <h3 className="font-bold">{supplier.name}</h3>
            <p className="text-gray-600">{supplier.contact_info}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

---

## 🚀 Переваги нової архітектури

1. **Розділення frontend та backend**
   - Backend може використовуватися з різних клієнтів
   - Frontend легко оновлювати та масштабувати

2. **Сучасний UI/UX**
   - React + Tailwind CSS = швидка розробка красивого інтерфейсу
   - Адаптивний дизайн (mobile-friendly)

3. **Автоматична документація API**
   - Swagger UI на `/docs`
   - Легко тестувати API

4. **Безпека**
   - HTTP Basic Auth (можна легко змінити на JWT)
   - CORS налаштування

5. **Продуктивність**
   - FastAPI - один з найшвидших Python фреймворків
   - React - ефективне оновлення UI

---

## 📝 TODO для завершення міграції

- [ ] Створити React проект
- [ ] Налаштувати Tailwind CSS
- [ ] Створити API клієнт (services)
- [ ] Створити компоненти для кожного модуля:
  - [ ] Постачальники
  - [ ] Комплектуючі
  - [ ] Склади
  - [ ] Замовлення
  - [ ] Комірники
  - [ ] Поставки
- [ ] Створити роутинг (react-router-dom)
- [ ] Додати форми з валідацією
- [ ] Стилізувати з Tailwind CSS
- [ ] Підключити до backend API
- [ ] Тестування

---

## 🎯 Швидкий старт (10 хвилин)

1. **Запустити backend:**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python run.py
   ```

2. **Створити frontend:**
   ```bash
   npm create vite@latest frontend -- --template react
   cd frontend
   npm install
   npm install axios react-router-dom tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

3. **Відкрити два термінали:**
   - Terminal 1: Backend (port 8000)
   - Terminal 2: Frontend (`npm run dev` - port 5173)

4. **Тестувати:**
   - Backend API: http://localhost:8000/docs
   - Frontend: http://localhost:5173

---

## 💡 Поради

- Використовуйте **React Query** для кешування даних
- Додайте **React Hook Form** для форм
- Використовуйте **Heroicons** або **Lucide React** для іконок
- Додайте **toast notifications** (react-hot-toast)
- Налаштуйте **ESLint** та **Prettier**

---

Успіхів з міграцією! 🚀
```

---

## Root

### `db\__init__.py`

```python

```

### `db\database.py`

```python
import sqlite3
import os

# Шлях за замовчуванням
DEFAULT_DB_FILENAME = "supply.db"
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), DEFAULT_DB_FILENAME)

def get_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """
    Повертає підключення до SQLite, з увімкненими foreign_keys
    і row_factory=sqlite3.Row.
    Параметр db_path дозволяє вказати шлях до іншої БД (для тестування).
    """
    if db_path != ":memory:":
        # Переконаємося, що директорія існує (якщо БД у підпапці)
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn
```

### `requirements.txt`

```text
sqlalchemy==2.0.29
fpdf==1.7.2
PyPDF2==3.0.1
pytest==8.2.0
python-dateutil==2.9.0

```

---

## Backend - Config

### `backend\app\__init__.py`

```python

```

### `backend\app\main.py`

```python
"""FastAPI main application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .api import suppliers, components, warehouses, orders, storekeepers, supplies

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Інформаційна система для відділу комплектації підприємства"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(suppliers.router, prefix=settings.API_PREFIX)
app.include_router(components.router, prefix=settings.API_PREFIX)
app.include_router(warehouses.router, prefix=settings.API_PREFIX)
app.include_router(orders.router, prefix=settings.API_PREFIX)
app.include_router(storekeepers.router, prefix=settings.API_PREFIX)
app.include_router(supplies.router, prefix=settings.API_PREFIX)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Supply Management System API",
        "version": settings.VERSION,
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
```

### `backend\fix_all_imports.py`

```python
"""Fix all imports in backend app."""
import os
import re

def fix_file(filepath, replacements):
    """Fix imports in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        for old, new in replacements:
            content = re.sub(old, new, content, flags=re.MULTILINE)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Fixed: {filepath}")
            return True
        return False
    except Exception as e:
        print(f"[ERROR] in {filepath}: {e}")
        return False

def fix_all():
    """Fix all imports."""
    # DAO files - fix base_dao imports
    dao_replacements = [
        (r'^from dao\.base_dao import', 'from .base_dao import'),
        (r'^from dao\.', 'from .'),
        (r'^from models\.', 'from ..models.'),
        (r'^from db\.database', 'from ..db.database'),
    ]

    dao_dir = 'app/dao'
    if os.path.exists(dao_dir):
        print("\n=== Fixing DAO files ===")
        for filename in os.listdir(dao_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                fix_file(os.path.join(dao_dir, filename), dao_replacements)

    # Services files
    services_replacements = [
        (r'^from dao\.', 'from ..dao.'),
        (r'^from models\.', 'from ..models.'),
        (r'^from services\.', 'from .'),
    ]

    services_dir = 'app/services'
    if os.path.exists(services_dir):
        print("\n=== Fixing Services files ===")
        for filename in os.listdir(services_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                fix_file(os.path.join(services_dir, filename), services_replacements)

if __name__ == '__main__':
    print("Fixing all imports in backend app...")
    fix_all()
    print("\n[DONE] All imports fixed!")
```

### `backend\fix_imports.py`

```python
"""Fix imports in copied files."""
import os
import re

def fix_imports_in_file(filepath, patterns):
    """Fix imports in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for old_pattern, new_pattern in patterns:
        content = re.sub(old_pattern, new_pattern, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
        return True
    return False

def fix_services():
    """Fix imports in services directory."""
    patterns = [
        (r'^from dao\.', 'from ..dao.', re.MULTILINE),
        (r'^from models\.', 'from ..models.', re.MULTILINE),
    ]

    services_dir = 'app/services'
    for filename in os.listdir(services_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(services_dir, filename)
            try:
                for old, new, flags in patterns:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = re.sub(old, new, content, flags=flags)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                print(f"Fixed: {filepath}")
            except Exception as e:
                print(f"Error fixing {filepath}: {e}")

def fix_dao():
    """Fix imports in dao directory."""
    patterns = [
        (r'^from models\.', 'from ..models.', re.MULTILINE),
        (r'^from db\.database', 'from ..db.database', re.MULTILINE),
    ]

    dao_dir = 'app/dao'
    for filename in os.listdir(dao_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(dao_dir, filename)
            try:
                for old, new, flags in patterns:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = re.sub(old, new, content, flags=flags)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                print(f"Fixed: {filepath}")
            except Exception as e:
                print(f"Error fixing {filepath}: {e}")

if __name__ == '__main__':
    print("Fixing imports...")
    fix_services()
    fix_dao()
    print("Done!")
```

### `backend\README.md`

```markdown
# Backend - FastAPI Application

## Встановлення

1. Створіть віртуальне середовище:
```bash
python -m venv venv
```

2. Активуйте віртуальне середовище:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Встановіть залежності:
```bash
pip install -r requirements.txt
```

## Запуск

```bash
python run.py
```

Сервер запуститься на `http://localhost:8000`

## API Документація

Після запуску сервера, документація API доступна за адресою:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Автентифікація

Базова HTTP автентифікація з наступними користувачами:

- **Admin**: username: `admin`, password: `admin`
- **User**: username: `user`, password: `user`

## Endpoints

### Suppliers
- `GET /api/v1/suppliers/` - Отримати всіх постачальників
- `POST /api/v1/suppliers/` - Створити постачальника
- `GET /api/v1/suppliers/{id}` - Отримати постачальника за ID
- `PUT /api/v1/suppliers/{id}` - Оновити постачальника
- `DELETE /api/v1/suppliers/{id}` - Видалити постачальника

### Components
- `GET /api/v1/components/` - Отримати всі комплектуючі
- `POST /api/v1/components/` - Створити комплектуюче
- `GET /api/v1/components/{id}` - Отримати комплектуюче за ID
- `PUT /api/v1/components/{id}` - Оновити комплектуюче
- `DELETE /api/v1/components/{id}` - Видалити комплектуюче

### Warehouses
- `GET /api/v1/warehouses/` - Отримати всі склади
- `GET /api/v1/warehouses/stock-levels` - Отримати залишки
- `POST /api/v1/warehouses/` - Створити склад
- `GET /api/v1/warehouses/{id}` - Отримати склад за ID
- `PUT /api/v1/warehouses/{id}` - Оновити склад
- `DELETE /api/v1/warehouses/{id}` - Видалити склад
```

### `backend\requirements.txt`

```text
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.5.3
pydantic-settings==2.1.0
python-multipart==0.0.6
```

### `backend\run.py`

```python
"""Run the FastAPI application."""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
```

---

## Backend - Core

### `backend\app\core\__init__.py`

```python

```

### `backend\app\core\auth.py`

```python
"""Basic authentication for the application."""
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

# Simple hardcoded users for basic auth (без bcrypt для спрощення)
USERS_DB = {
    "admin": {
        "username": "admin",
        "password": "admin",  # В продакшені використовуйте хешовані паролі!
        "full_name": "Administrator",
        "role": "admin"
    },
    "user": {
        "username": "user",
        "password": "user",  # В продакшені використовуйте хешовані паролі!
        "full_name": "Regular User",
        "role": "user"
    }
}


def authenticate_user(username: str, password: str) -> Optional[dict]:
    """Authenticate a user."""
    user = USERS_DB.get(username)
    if not user:
        return None
    # Проста перевірка пароля (в продакшені використовуйте хешування!)
    if password != user["password"]:
        return None
    return user


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> dict:
    """Get current authenticated user."""
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


# Optional dependency - can be used to protect routes
def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    """Get current active user."""
    return current_user
```

### `backend\app\core\config.py`

```python
"""Application configuration."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "Supply Management System"
    VERSION: str = "2.0.0"
    API_PREFIX: str = "/api/v1"

    # CORS settings
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]

    # Database
    DATABASE_PATH: str = "../db/supply.db"

    class Config:
        case_sensitive = True


settings = Settings()
```

### `backend\app\core\dependencies.py`

```python
"""Dependencies for FastAPI routes."""
from typing import Generator
import sqlite3


def get_db() -> Generator:
    """Get database connection."""
    try:
        conn = sqlite3.connect("../../db/supply.db")
        conn.row_factory = sqlite3.Row
        yield conn
    finally:
        conn.close()
```

---

## Backend - Database

### `backend\app\db\__init__.py`

```python

```

### `backend\app\db\database.py`

```python
import sqlite3
import os

# Шлях за замовчуванням
DEFAULT_DB_FILENAME = "supply.db"
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), DEFAULT_DB_FILENAME)

def get_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """
    Повертає підключення до SQLite, з увімкненими foreign_keys
    і row_factory=sqlite3.Row.
    Параметр db_path дозволяє вказати шлях до іншої БД (для тестування).
    """
    if db_path != ":memory:":
        # Переконаємося, що директорія існує (якщо БД у підпапці)
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn
```

### `backend\db\__init__.py`

```python

```

### `backend\db\database.py`

```python
import sqlite3
import os

# Шлях за замовчуванням
DEFAULT_DB_FILENAME = "supply.db"
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), DEFAULT_DB_FILENAME)

def get_connection(db_path: str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """
    Повертає підключення до SQLite, з увімкненими foreign_keys
    і row_factory=sqlite3.Row.
    Параметр db_path дозволяє вказати шлях до іншої БД (для тестування).
    """
    if db_path != ":memory:":
        # Переконаємося, що директорія існує (якщо БД у підпапці)
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn
```

---

## Backend - Models

### `backend\app\models\__init__.py`

```python

```

### `backend\app\models\component.py`

```python

from dataclasses import dataclass
from typing import Optional

@dataclass
class Component:
    name: str
    unit: str
    quantity_in_stock: int = 0
    id: Optional[int] = None

    def get_info(self) -> str:
        return f"{self.name} ({self.unit}), на складі: {self.quantity_in_stock}"

    def validate(self) -> bool:
        return bool(self.name.strip() and self.unit.strip())
```

### `backend\app\models\order.py`

```python
from dataclasses import dataclass, field
from typing import List
from .supply_record import SupplyRecord

@dataclass
class Order:
    items: List[SupplyRecord] = field(default_factory=list)

    def add_item(self, record: SupplyRecord) -> None:
        self.items.append(record)

    def calculate_total(self) -> float:
        return sum(item.get_line_cost() for item in self.items)

    def __str__(self) -> str:
        lines = ["=== Замовлення ==="]
        for i, item in enumerate(self.items, 1):
            lines.append(
                f"{i}) Компонент ID: {item.component_id}, Кількість: {item.quantity}, Ціна: {item.price}"
            )
        lines.append(f"Загальна вартість: {self.calculate_total():.2f}")
        return "\n".join(lines)
```

### `backend\app\models\storekeeper.py`

```python

from dataclasses import dataclass
from typing import Optional

@dataclass
class Storekeeper:
    name: str
    warehouse_id: int
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"{self.name} (Склад ID: {self.warehouse_id})"

    def validate(self) -> bool:
        return bool(self.name.strip() and isinstance(self.warehouse_id, int))
```

### `backend\app\models\supplier.py`

```python

from dataclasses import dataclass
from typing import Optional

@dataclass
class Supplier:
    name: str
    contact_info: str = ""
    id: Optional[int] = None

    def get_details(self) -> str:
        return f"Постачальник: {self.name}, Контакт: {self.contact_info}"

    def validate(self) -> bool:
        return bool(self.name.strip())
```

### `backend\app\models\supply.py`

```python

from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Supply:
    supply_date: date
    supplier_id: int
    warehouse_id: int
    storekeeper_id: int
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"Поставка {self.id} від {self.supply_date}"
```

### `backend\app\models\supply_record.py`

```python

from dataclasses import dataclass
from typing import Optional

@dataclass
class SupplyRecord:
    supply_id: int
    component_id: int
    quantity: int
    price: float
    id: Optional[int] = None

    def get_line_cost(self) -> float:
        return self.quantity * self.price

    def __str__(self) -> str:
        return f"Компонент {self.component_id} x {self.quantity} за {self.price}"
```

### `backend\app\models\warehouse.py`

```python

from dataclasses import dataclass
from typing import Optional

@dataclass
class Warehouse:
    name: str
    location: str
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"{self.name} ({self.location})"

    def validate(self) -> bool:
        return bool(self.name.strip() and self.location.strip())
```

---

## Backend - DAO

### `backend\app\dao\__init__.py`

```python

```

### `backend\app\dao\base_dao.py`

```python
"""Base DAO class with common interface for all data access objects."""
import sqlite3
from abc import ABC, abstractmethod
from typing import Optional, Any


class BaseDAO(ABC):
    """Abstract base class for all DAO implementations.

    Provides a consistent interface for CRUD operations across all entities.
    All DAOs should return dictionaries for consistency and serialization.
    """

    def __init__(self, conn: sqlite3.Connection):
        """Initialize DAO with database connection.

        Args:
            conn: SQLite database connection with foreign_keys enabled.
        """
        self.conn = conn
        self._ensure_table()

    @abstractmethod
    def _ensure_table(self):
        """Create table if it doesn't exist. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def insert(self, data: dict) -> int:
        """Insert a new record.

        Args:
            data: Dictionary with entity fields.

        Returns:
            ID of the inserted record.
        """
        pass

    @abstractmethod
    def update(self, data: dict) -> bool:
        """Update an existing record.

        Args:
            data: Dictionary with entity fields including 'id'.

        Returns:
            True if record was updated, False otherwise.
        """
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        """Delete a record by ID.

        Args:
            entity_id: ID of the record to delete.

        Returns:
            True if record was deleted, False otherwise.
        """
        pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find a record by ID.

        Args:
            entity_id: ID of the record to find.

        Returns:
            Dictionary with entity fields or None if not found.
        """
        pass

    @abstractmethod
    def find_all(self) -> list[dict]:
        """Find all records.

        Returns:
            List of dictionaries with entity fields.
        """
        pass

    def _row_to_dict(self, row: sqlite3.Row, fields: list[str]) -> dict:
        """Convert database row to dictionary.

        Args:
            row: Database row from cursor.fetchone().
            fields: List of field names in order.

        Returns:
            Dictionary mapping field names to values.
        """
        if row is None:
            return None
        return {field: row[i] for i, field in enumerate(fields)}

    def _rows_to_dicts(self, rows: list[sqlite3.Row], fields: list[str]) -> list[dict]:
        """Convert multiple database rows to list of dictionaries.

        Args:
            rows: List of database rows from cursor.fetchall().
            fields: List of field names in order.

        Returns:
            List of dictionaries mapping field names to values.
        """
        return [self._row_to_dict(row, fields) for row in rows]
```

### `backend\app\dao\component_dao.py`

```python
import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.component import Component


class ComponentDAO(BaseDAO):
    """SQLite-based DAO for components.

    Returns all data as dictionaries for consistency.
    Provides additional method for updating stock quantity.
    """

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS components (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                unit TEXT NOT NULL,
                quantity_in_stock INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new component.

        Args:
            data: Dictionary with 'name', 'unit', and optional 'quantity_in_stock'.

        Returns:
            ID of the inserted component.
        """
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO components (name, unit, quantity_in_stock) VALUES (?, ?, ?)",
                (data["name"], data["unit"], data.get("quantity_in_stock", 0)),
            )
        return cur.lastrowid

    def find_all(self) -> list[dict]:
        """Find all components ordered by ID.

        Returns:
            List of dictionaries with component data.
        """
        cur = self.conn.execute("SELECT id, name, unit, quantity_in_stock FROM components ORDER BY id")
        return self._rows_to_dicts(cur.fetchall(), ["id", "name", "unit", "quantity_in_stock"])

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find component by ID.

        Args:
            entity_id: ID of the component.

        Returns:
            Dictionary with component data or None if not found.
        """
        cur = self.conn.execute(
            "SELECT id, name, unit, quantity_in_stock FROM components WHERE id = ?",
            (entity_id,),
        )
        row = cur.fetchone()
        return self._row_to_dict(row, ["id", "name", "unit", "quantity_in_stock"])

    def update(self, data: dict) -> bool:
        """Update an existing component.

        Args:
            data: Dictionary with 'id', 'name', 'unit', and 'quantity_in_stock'.

        Returns:
            True if component was updated, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute(
                "UPDATE components SET name = ?, unit = ?, quantity_in_stock = ? WHERE id = ?",
                (data["name"], data["unit"], data["quantity_in_stock"], data["id"]),
            )
        return cur.rowcount > 0

    def update_quantity(self, comp_id: int, delta: int) -> None:
        """Update component stock quantity by delta.

        Args:
            comp_id: ID of the component.
            delta: Amount to add (or subtract if negative) from current stock.
        """
        with self.conn:
            self.conn.execute(
                "UPDATE components SET quantity_in_stock = quantity_in_stock + ? WHERE id = ?",
                (delta, comp_id),
            )

    def delete(self, entity_id: int) -> bool:
        """Delete a component by ID.

        Args:
            entity_id: ID of the component to delete.

        Returns:
            True if component was deleted, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute("DELETE FROM components WHERE id = ?", (entity_id,))
        return cur.rowcount > 0
```

### `backend\app\dao\contract_dao.py`

```python
class ContractDAO:
    def __init__(self, conn=None):
        self.conn = conn

    def insert(self, dto):
        pass

    def select_all(self):
        return []

    def find_by_id(self, contract_id):
        return None
```

### `backend\app\dao\history_dao.py`

```python
class HistoryDAO:
    def __init__(self, conn=None):
        self.conn = conn

    def insert(self, dto):
        pass

    def select_all(self):
        return []

    def find_by_id(self, history_id):
        return None
```

### `backend\app\dao\order_dao.py`

```python
class OrderDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, dto):
        pass

    def select_all(self):
        return []

    def find_by_id(self, order_id):
        return None
```

### `backend\app\dao\storekeeper_dao.py`

```python
import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.storekeeper import Storekeeper


class StorekeeperDAO(BaseDAO):
    """SQLite-based DAO for storekeepers.

    Returns all data as dictionaries for consistency.
    """

    def _ensure_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS storekeepers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                warehouse_id INTEGER,
                FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
            )
        """)
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new storekeeper.

        Args:
            data: Dictionary with 'name' and optional 'warehouse_id'.

        Returns:
            ID of the inserted storekeeper.
        """
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO storekeepers (name, warehouse_id) VALUES (?, ?)",
                (data["name"], data.get("warehouse_id"))
            )
        return cursor.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing storekeeper.

        Args:
            data: Dictionary with 'id', 'name', and optional 'warehouse_id'.

        Returns:
            True if storekeeper was updated, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE storekeepers SET name = ?, warehouse_id = ? WHERE id = ?",
                (data["name"], data.get("warehouse_id"), data["id"])
            )
        return cursor.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a storekeeper by ID.

        Args:
            entity_id: ID of the storekeeper to delete.

        Returns:
            True if storekeeper was deleted, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM storekeepers WHERE id = ?",
                (entity_id,)
            )
        return cursor.rowcount > 0

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find storekeeper by ID.

        Args:
            entity_id: ID of the storekeeper.

        Returns:
            Dictionary with storekeeper data or None if not found.
        """
        cursor = self.conn.execute(
            "SELECT id, name, warehouse_id FROM storekeepers WHERE id = ?",
            (entity_id,)
        )
        row = cursor.fetchone()
        return self._row_to_dict(row, ["id", "name", "warehouse_id"])

    def find_all(self) -> list[dict]:
        """Find all storekeepers ordered by name.

        Returns:
            List of dictionaries with storekeeper data.
        """
        cursor = self.conn.execute(
            "SELECT id, name, warehouse_id FROM storekeepers ORDER BY name"
        )
        return self._rows_to_dicts(cursor.fetchall(), ["id", "name", "warehouse_id"])
```

### `backend\app\dao\supplier_dao.py`

```python
import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.supplier import Supplier


class SupplierDAO(BaseDAO):
    """SQLite-based DAO for suppliers.

    Returns all data as dictionaries for consistency.
    """

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_info TEXT
            )
            """
        )
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new supplier.

        Args:
            data: Dictionary with 'name' and optional 'contact_info'.

        Returns:
            ID of the inserted supplier.
        """
        cur = self.conn.execute(
            "INSERT INTO suppliers (name, contact_info) VALUES (?, ?)",
            (data["name"], data.get("contact_info", "")),
        )
        self.conn.commit()
        return cur.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing supplier.

        Args:
            data: Dictionary with 'id', 'name', and optional 'contact_info'.

        Returns:
            True if supplier was updated, False otherwise.
        """
        cur = self.conn.execute(
            "UPDATE suppliers SET name = ?, contact_info = ? WHERE id = ?",
            (data["name"], data.get("contact_info", ""), data["id"]),
        )
        self.conn.commit()
        return cur.rowcount > 0



    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find supplier by ID.

        Args:
            entity_id: ID of the supplier.

        Returns:
            Dictionary with supplier data or None if not found.
        """
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE id = ?",
            (entity_id,),
        )
        row = cur.fetchone()
        return self._row_to_dict(row, ["id", "name", "contact_info"])

    def find_all(self) -> list[dict]:
        """Find all suppliers ordered by name.

        Returns:
            List of dictionaries with supplier data.
        """
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers ORDER BY name"
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "name", "contact_info"])

    def find_by_name(self, name_part: str) -> list[dict]:
        """Find suppliers by partial name match.

        Args:
            name_part: Partial name to search for.

        Returns:
            List of dictionaries with matching suppliers.
        """
        pattern = f"%{name_part}%"
        cur = self.conn.execute(
            "SELECT id, name, contact_info FROM suppliers WHERE name LIKE ?",
            (pattern,),
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "name", "contact_info"])

    def delete(self, entity_id: int) -> bool:
        """Delete a supplier by ID.

        Args:
            entity_id: ID of the supplier to delete.

        Returns:
            True if supplier was deleted, False otherwise.
        """
        cur = self.conn.execute("DELETE FROM suppliers WHERE id = ?", (entity_id,))
        self.conn.commit()
        return cur.rowcount > 0
```

### `backend\app\dao\supply_dao.py`

```python
import sqlite3
from typing import Optional
from datetime import datetime

from .base_dao import BaseDAO
from ..models.supply import Supply


class SupplyDAO(BaseDAO):
    """SQLite-based DAO for supplies.

    Returns all data as dictionaries for consistency.
    Handles date serialization to/from ISO format.
    """

    def _ensure_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS supplies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                supplier_id INTEGER,
                warehouse_id INTEGER,
                storekeeper_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (warehouse_id) REFERENCES warehouses(id),
                FOREIGN KEY (storekeeper_id) REFERENCES storekeepers(id)
            )
        """)
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new supply.

        Args:
            data: Dictionary with 'supply_date' (date or str), 'supplier_id',
                  'warehouse_id', and 'storekeeper_id'.

        Returns:
            ID of the inserted supply.
        """
        # Convert date to ISO string if needed
        date_str = data["supply_date"]
        if hasattr(date_str, "isoformat"):
            date_str = date_str.isoformat()

        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO supplies (date, supplier_id, warehouse_id, storekeeper_id)
            VALUES (?, ?, ?, ?)
        """, (date_str, data["supplier_id"], data["warehouse_id"], data["storekeeper_id"]))
        self.conn.commit()
        return cursor.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing supply.

        Args:
            data: Dictionary with 'id', 'supply_date', 'supplier_id',
                  'warehouse_id', and 'storekeeper_id'.

        Returns:
            True if supply was updated, False otherwise.
        """
        # Convert date to ISO string if needed
        date_str = data["supply_date"]
        if hasattr(date_str, "isoformat"):
            date_str = date_str.isoformat()

        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE supplies SET date = ?, supplier_id = ?, warehouse_id = ?, storekeeper_id = ?
            WHERE id = ?
        """, (date_str, data["supplier_id"], data["warehouse_id"], data["storekeeper_id"], data["id"]))
        self.conn.commit()
        return cursor.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a supply by ID.

        Args:
            entity_id: ID of the supply to delete.

        Returns:
            True if supply was deleted, False otherwise.
        """
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM supplies WHERE id = ?", (entity_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def find_all(self) -> list[dict]:
        """Find all supplies.

        Returns:
            List of dictionaries with supply data (dates as ISO strings).
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, date, supplier_id, warehouse_id, storekeeper_id FROM supplies ORDER BY date DESC")
        rows = cursor.fetchall()
        return self._rows_to_dicts(rows, ["id", "supply_date", "supplier_id", "warehouse_id", "storekeeper_id"])

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find supply by ID.

        Args:
            entity_id: ID of the supply.

        Returns:
            Dictionary with supply data or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, date, supplier_id, warehouse_id, storekeeper_id FROM supplies WHERE id = ?", (entity_id,))
        row = cursor.fetchone()
        return self._row_to_dict(row, ["id", "supply_date", "supplier_id", "warehouse_id", "storekeeper_id"])
```

### `backend\app\dao\supply_record_dao.py`

```python
import sqlite3
import logging
from typing import Optional

from .base_dao import BaseDAO
from ..models.supply_record import SupplyRecord

logger = logging.getLogger(__name__)


class SupplyRecordDAO(BaseDAO):
    """SQLite-based DAO for supply records.

    Returns all data as dictionaries for consistency.
    Supports Observer pattern for inventory updates.

    Args:
        conn: SQLite database connection.
        observer: Optional object with update(record_data: dict) method.
                  Called after successful insert.
    """

    def __init__(self, conn: sqlite3.Connection, observer: Optional[object] = None):
        self.observer = observer
        super().__init__(conn)

    def _ensure_table(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS supply_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supply_id INTEGER,
                component_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (supply_id) REFERENCES supplies(id),
                FOREIGN KEY (component_id) REFERENCES components(id)
            )
            """
        )
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new supply record.

        Args:
            data: Dictionary with 'supply_id', 'component_id', 'quantity', 'price'.

        Returns:
            ID of the inserted record.
        """
        with self.conn:
            cur = self.conn.execute(
                """INSERT INTO supply_records
                       (supply_id, component_id, quantity, price)
                       VALUES (?,?,?,?)""",
                (data["supply_id"], data["component_id"], data["quantity"], data["price"]),
            )
            record_id = cur.lastrowid

        # Notify observer with complete record data
        if self.observer and hasattr(self.observer, "update"):
            try:
                record_data = {**data, "id": record_id}
                self.observer.update(record_data)
            except Exception as e:
                logger.error(f"Observer update failed: {e}")

        return record_id

    def update(self, data: dict) -> bool:
        """Update an existing supply record.

        Args:
            data: Dictionary with 'id', 'supply_id', 'component_id', 'quantity', 'price'.

        Returns:
            True if record was updated, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute(
                """UPDATE supply_records
                   SET supply_id = ?, component_id = ?, quantity = ?, price = ?
                   WHERE id = ?""",
                (data["supply_id"], data["component_id"], data["quantity"], data["price"], data["id"]),
            )
        return cur.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a supply record by ID.

        Args:
            entity_id: ID of the record to delete.

        Returns:
            True if record was deleted, False otherwise.
        """
        with self.conn:
            cur = self.conn.execute("DELETE FROM supply_records WHERE id = ?", (entity_id,))
        return cur.rowcount > 0

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find supply record by ID.

        Args:
            entity_id: ID of the record.

        Returns:
            Dictionary with record data or None if not found.
        """
        cur = self.conn.execute(
            """SELECT id, supply_id, component_id, quantity, price
               FROM supply_records WHERE id = ?""",
            (entity_id,),
        )
        row = cur.fetchone()
        return self._row_to_dict(row, ["id", "supply_id", "component_id", "quantity", "price"])

    def find_all(self) -> list[dict]:
        """Find all supply records.

        Returns:
            List of dictionaries with record data.
        """
        cur = self.conn.execute(
            """SELECT id, supply_id, component_id, quantity, price
               FROM supply_records ORDER BY id"""
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "supply_id", "component_id", "quantity", "price"])

    def find_by_supply(self, supply_id: int) -> list[dict]:
        """Find all records for a specific supply.

        Args:
            supply_id: ID of the supply.

        Returns:
            List of dictionaries with record data.
        """
        cur = self.conn.execute(
            """SELECT id, supply_id, component_id, quantity, price
                   FROM supply_records
                   WHERE supply_id = ?""",
            (supply_id,),
        )
        return self._rows_to_dicts(cur.fetchall(), ["id", "supply_id", "component_id", "quantity", "price"])
```

### `backend\app\dao\warehouse_dao.py`

```python
import sqlite3
from typing import Optional

from .base_dao import BaseDAO
from ..models.warehouse import Warehouse


class WarehouseDAO(BaseDAO):
    """SQLite-based DAO for warehouses.

    Returns all data as dictionaries for consistency.
    """

    def _ensure_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS warehouses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT
            )
        """)
        self.conn.commit()

    def insert(self, data: dict) -> int:
        """Insert a new warehouse.

        Args:
            data: Dictionary with 'name' and optional 'location'.

        Returns:
            ID of the inserted warehouse.
        """
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO warehouses (name, location) VALUES (?, ?)",
                (data["name"], data.get("location", ""))
            )
        return cursor.lastrowid

    def update(self, data: dict) -> bool:
        """Update an existing warehouse.

        Args:
            data: Dictionary with 'id', 'name', and optional 'location'.

        Returns:
            True if warehouse was updated, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "UPDATE warehouses SET name = ?, location = ? WHERE id = ?",
                (data["name"], data.get("location", ""), data["id"])
            )
        return cursor.rowcount > 0

    def delete(self, entity_id: int) -> bool:
        """Delete a warehouse by ID.

        Args:
            entity_id: ID of the warehouse to delete.

        Returns:
            True if warehouse was deleted, False otherwise.
        """
        with self.conn:
            cursor = self.conn.execute(
                "DELETE FROM warehouses WHERE id = ?",
                (entity_id,)
            )
        return cursor.rowcount > 0

    def find_by_id(self, entity_id: int) -> Optional[dict]:
        """Find warehouse by ID.

        Args:
            entity_id: ID of the warehouse.

        Returns:
            Dictionary with warehouse data or None if not found.
        """
        cursor = self.conn.execute(
            "SELECT id, name, location FROM warehouses WHERE id = ?",
            (entity_id,)
        )
        row = cursor.fetchone()
        return self._row_to_dict(row, ["id", "name", "location"])

    def find_all(self) -> list[dict]:
        """Find all warehouses ordered by name.

        Returns:
            List of dictionaries with warehouse data.
        """
        cursor = self.conn.execute(
            "SELECT id, name, location FROM warehouses ORDER BY name"
        )
        return self._rows_to_dicts(cursor.fetchall(), ["id", "name", "location"])
```

---

## Backend - Services

### `backend\app\services\__init__.py`

```python

```

### `backend\app\services\component_service.py`

```python
from ..dao.component_dao import ComponentDAO
from ..models.component import Component


class ComponentService:
    """Facade over ComponentDAO with validation and model conversion."""

    def __init__(self, dao: ComponentDAO):
        self.dao = dao

    def create(self, data: dict) -> int:
        """Create a new component.

        Args:
            data: Dictionary with 'name', 'unit', and 'qty' (or 'quantity_in_stock').

        Returns:
            ID of the created component.

        Raises:
            ValueError: If component data is invalid.
        """
        # Normalize field names - accept both 'qty' and 'quantity_in_stock'
        quantity = data.get("qty", data.get("quantity_in_stock", 0))

        comp = Component(
            name=data.get("name", ""),
            unit=data.get("unit", ""),
            quantity_in_stock=quantity
        )

        if not comp.validate():
            raise ValueError("Invalid component data")

        dao_data = {"name": comp.name, "unit": comp.unit, "quantity_in_stock": comp.quantity_in_stock}
        return self.dao.insert(dao_data)

    def list_all(self) -> list[dict]:
        """Get all components as dictionaries.

        Returns:
            List of dictionaries with component data.
        """
        return self.dao.find_all()

    def get_by_id(self, comp_id: int) -> Component:
        """Get component by ID.

        Args:
            comp_id: ID of the component.

        Returns:
            Component instance.

        Raises:
            ValueError: If component not found.
        """
        data = self.dao.find_by_id(comp_id)
        if data is None:
            raise ValueError("Component not found")
        return Component(**data)

    def update(self, comp_id: int, data: dict) -> bool:
        """Update an existing component.

        Args:
            comp_id: ID of the component to update.
            data: Dictionary with 'name', 'unit', and 'qty' (or 'quantity_in_stock').

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If component data is invalid.
        """
        # Normalize field names - accept both 'qty' and 'quantity_in_stock'
        quantity = data.get("qty", data.get("quantity_in_stock", 0))

        comp = Component(
            id=comp_id,
            name=data.get("name", ""),
            unit=data.get("unit", ""),
            quantity_in_stock=quantity
        )

        if not comp.validate():
            raise ValueError("Invalid component data")

        dao_data = {"id": comp.id, "name": comp.name, "unit": comp.unit, "quantity_in_stock": comp.quantity_in_stock}
        return self.dao.update(dao_data)

    def delete(self, comp_id: int) -> bool:
        """Delete a component.

        Args:
            comp_id: ID of the component to delete.

        Returns:
            True if deleted successfully.
        """
        return self.dao.delete(comp_id)

    def increment_stock(self, component_id: int, delta: int) -> None:
        """Increase stock quantity for a component.

        Args:
            component_id: ID of the component.
            delta: Amount to add to stock (can be negative).

        Raises:
            ValueError: If parameters are invalid.
        """
        if not isinstance(component_id, int) or not isinstance(delta, int):
            raise ValueError("component_id and delta must be integers")
        self.dao.update_quantity(component_id, delta)
```

### `backend\app\services\contract_service.py`

```python
from ..dao.contract_dao import ContractDAO

class ContractService:
    """Фасад для валідації контрактів постачальників."""
    def __init__(self, contract_dao: ContractDAO):
        self.contract_dao = contract_dao

    def validate_contract(self, contract_id: int):
        """Може перевіряти, чи контракт містить усю необхідну контактну інформацію."""
        contract = self.contract_dao.find_by_id(contract_id)
        # Тут може бути додаткова логіка
        return contract is not None and contract.contact_info != ""

    def verify(self, contract_id: int):
        return self.validate_contract(contract_id)
```

### `backend\app\services\history_service.py`

```python
class HistoryService:
    def __init__(self, history_dao):
        self.history_dao = history_dao

    def get_history(self, filters=None):
        """Return supply history records from DAO."""
        if hasattr(self.history_dao, "fetch_records"):
            return self.history_dao.fetch_records(filters)
        return self.history_dao.select_all()

    def list_all(self):
        return self.history_dao.select_all()
```

### `backend\app\services\inventory_observer.py`

```python
import logging

from ..dao.component_dao import ComponentDAO

logger = logging.getLogger(__name__)


class InventoryObserver:
    """Updates component inventory after supply record insertion.

    Implements Observer pattern to automatically increment stock levels
    when new supply records are added.
    """

    def __init__(self, component_dao: ComponentDAO):
        self.component_dao = component_dao

    def update(self, record_data: dict):
        """Update component inventory based on supply record.

        Args:
            record_data: Dictionary with 'component_id' and 'quantity' keys.
        """
        component_id = record_data["component_id"]
        quantity = record_data["quantity"]

        self.component_dao.update_quantity(component_id, quantity)
        logger.info(f"Inventory updated: +{quantity} for component {component_id}")
```

### `backend\app\services\order_service.py`

```python
from ..dao.order_dao import OrderDAO


class OrderService:
    """Facade for order management via DAO."""

    def __init__(self, order_dao: OrderDAO):
        self.order_dao = order_dao

    def create(self, dto: dict) -> dict:
        order_id = self.order_dao.insert(dto)
        dto = dict(dto)
        if order_id is not None:
            dto["id"] = order_id
        return dto

    def list_all(self) -> list[dict]:
        return self.order_dao.select_all()
```

### `backend\app\services\receipt_service.py`

```python
from ..dao.supply_dao import SupplyDAO
from ..dao.supply_record_dao import SupplyRecordDAO

class ReceiptService:
    """Фасад для отримання детальних чеків по поставках."""
    def __init__(self, supply_dao: SupplyDAO, record_dao: SupplyRecordDAO):
        self.supply_dao = supply_dao
        self.record_dao = record_dao

    def get_receipt(self, supply_id: int):
        """Повертає об'єкт поставки та всі записи по цій поставці."""
        supply = self.supply_dao.find_by_id(supply_id)
        records = self.record_dao.find_by_supply(supply_id)
        return {"supply": supply, "records": records}
```

### `backend\app\services\record_service.py`

```python
from ..dao.supply_record_dao import SupplyRecordDAO

class RecordService:
    """Фасад для маніпуляцій із записами поставок."""
    def __init__(self, record_dao: SupplyRecordDAO):
        self.record_dao = record_dao

    def add_record(self, record):
        return self.record_dao.insert(record)

    def delete_record(self, record_id: int):
        return self.record_dao.delete(record_id)

    def get_records_by_supply(self, supply_id: int):
        return self.record_dao.find_by_supply(supply_id)
```

### `backend\app\services\report_service.py`

```python
from strategy.csv_export_strategy import CSVExportStrategy
from strategy.pdf_export_strategy import PDFExportStrategy

class ReportService:
    def export(self, kind: str, rows, out_path="report.out"):
        if kind == "csv":
            strategy = CSVExportStrategy()
        elif kind == "pdf":
            strategy = PDFExportStrategy()
        else:
            raise ValueError("Unsupported export type")
        return strategy.export(rows, out_path)
```

### `backend\app\services\storekeeper_service.py`

```python
from ..dao.storekeeper_dao import StorekeeperDAO
from ..models.storekeeper import Storekeeper


class StorekeeperService:
    """Facade over StorekeeperDAO with validation and model conversion."""

    def __init__(self, dao: StorekeeperDAO):
        self.dao = dao

    def create(self, keeper: Storekeeper) -> int:
        """Create a new storekeeper.

        Args:
            keeper: Storekeeper model instance.

        Returns:
            ID of the created storekeeper.

        Raises:
            ValueError: If validation fails.
        """
        keeper.validate()
        data = {"name": keeper.name, "warehouse_id": keeper.warehouse_id}
        return self.dao.insert(data)

    def update(self, keeper: Storekeeper) -> bool:
        """Update an existing storekeeper.

        Args:
            keeper: Storekeeper model instance with ID.

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If validation fails or ID is missing.
        """
        if keeper.id is None:
            raise ValueError("Storekeeper must have ID before update")
        keeper.validate()
        data = {"id": keeper.id, "name": keeper.name, "warehouse_id": keeper.warehouse_id}
        return self.dao.update(data)

    def delete(self, kid: int) -> bool:
        """Delete a storekeeper.

        Args:
            kid: ID of the storekeeper to delete.

        Returns:
            True if deleted successfully.

        Raises:
            ValueError: If ID is not an integer.
        """
        if not isinstance(kid, int):
            raise ValueError("ID must be int")
        return self.dao.delete(kid)

    def get_by_id(self, kid: int) -> Storekeeper:
        """Get storekeeper by ID.

        Args:
            kid: ID of the storekeeper.

        Returns:
            Storekeeper instance.

        Raises:
            ValueError: If ID is invalid or storekeeper not found.
        """
        if not isinstance(kid, int):
            raise ValueError("ID must be int")
        data = self.dao.find_by_id(kid)
        if data is None:
            raise ValueError("Storekeeper not found")
        return Storekeeper(**data)

    def list_all(self) -> list[Storekeeper]:
        """Get all storekeepers as model instances.

        Returns:
            List of Storekeeper instances.
        """
        dicts = self.dao.find_all()
        return [Storekeeper(**d) for d in dicts]
```

### `backend\app\services\supplier_service.py`

```python
from ..dao.supplier_dao import SupplierDAO
from ..models.supplier import Supplier


class SupplierService:
    """Facade over SupplierDAO with validation and model conversion."""

    def __init__(self, dao: SupplierDAO):
        self.dao = dao

    def create(self, data: dict) -> int:
        """Create a new supplier from dictionary data.

        Args:
            data: Dictionary with 'name' and optional 'contact_info'.

        Returns:
            ID of the created supplier.

        Raises:
            ValueError: If validation fails.
        """
        # Validate using model
        supplier = Supplier(name=data["name"], contact_info=data.get("contact_info", ""))
        if not supplier.validate():
            raise ValueError("Invalid supplier data")

        return self.dao.insert(data)

    def list_all(self) -> list[Supplier]:
        """Get all suppliers as model instances.

        Returns:
            List of Supplier instances.
        """
        dicts = self.dao.find_all()
        return [Supplier(**d) for d in dicts]

    def get_by_id(self, supplier_id: int) -> Supplier:
        """Get supplier by ID.

        Args:
            supplier_id: ID of the supplier.

        Returns:
            Supplier instance.

        Raises:
            ValueError: If supplier not found.
        """
        data = self.dao.find_by_id(supplier_id)
        if data is None:
            raise ValueError("Supplier not found")
        return Supplier(**data)

    def update(self, data: dict) -> bool:
        """Update an existing supplier.

        Args:
            data: Dictionary with 'id', 'name', and optional 'contact_info'.

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If validation fails.
        """
        # Validate using model
        supplier = Supplier(id=data.get("id"), name=data["name"], contact_info=data.get("contact_info", ""))
        if not supplier.validate():
            raise ValueError("Invalid supplier data")

        return self.dao.update(data)

    def delete(self, supplier_id: int) -> bool:
        """Delete a supplier.

        Args:
            supplier_id: ID of the supplier to delete.

        Returns:
            True if deleted successfully.
        """
        return self.dao.delete(supplier_id)
```

### `backend\app\services\supply_service.py`

```python
from datetime import datetime

from ..dao.supply_dao import SupplyDAO
from ..dao.supply_record_dao import SupplyRecordDAO
from ..models.supply import Supply
from ..models.supply_record import SupplyRecord


class SupplyService:
    """Service for registering supplies with automatic inventory updates."""

    def __init__(self, supply_dao: SupplyDAO, record_dao: SupplyRecordDAO):
        self.supply_dao = supply_dao
        self.record_dao = record_dao

    def register(self, dto: dict) -> str:
        """Register a supply from dictionary data.

        Args:
            dto: Dictionary with 'supply' and 'records' keys.

        Returns:
            Success message.
        """
        supply: Supply = dto.get("supply")
        records: list[SupplyRecord] = dto.get("records", [])
        self.register_supply(supply, records)
        return "<<SupplySaved>>"

    def register_supply(self, supply: Supply, records: list[SupplyRecord]) -> int:
        """Register a supply with multiple records.

        Args:
            supply: Supply model instance.
            records: List of SupplyRecord instances.

        Returns:
            ID of the created supply.

        Raises:
            ValueError: If no records provided.
        """
        if not records:
            raise ValueError("Supply must contain at least one record")

        # Convert Supply to dict
        supply_data = {
            "supply_date": supply.supply_date,
            "supplier_id": supply.supplier_id,
            "warehouse_id": supply.warehouse_id,
            "storekeeper_id": supply.storekeeper_id
        }
        supply_id = self.supply_dao.insert(supply_data)
        supply.id = supply_id

        # Insert records (Observer will update inventory)
        for rec in records:
            rec.supply_id = supply_id
            record_data = {
                "supply_id": supply_id,
                "component_id": rec.component_id,
                "quantity": rec.quantity,
                "price": rec.price
            }
            record_id = self.record_dao.insert(record_data)
            rec.id = record_id

        return supply_id

    def list_all(self) -> list[Supply]:
        """Get all supplies as model instances.

        Returns:
            List of Supply instances.
        """
        dicts = self.supply_dao.find_all()
        supplies = []
        for d in dicts:
            # Convert ISO date string to date object
            date_str = d["supply_date"]
            if isinstance(date_str, str):
                d["supply_date"] = datetime.fromisoformat(date_str).date()
            supplies.append(Supply(**d))
        return supplies
```

### `backend\app\services\warehouse_service.py`

```python
from ..dao.warehouse_dao import WarehouseDAO
from ..models.warehouse import Warehouse


class WarehouseService:
    """Facade over WarehouseDAO with validation and model conversion."""

    def __init__(self, dao: WarehouseDAO):
        self.dao = dao

    def create(self, warehouse: Warehouse) -> int:
        """Create a new warehouse.

        Args:
            warehouse: Warehouse model instance.

        Returns:
            ID of the created warehouse.

        Raises:
            ValueError: If validation fails.
        """
        warehouse.validate()
        data = {"name": warehouse.name, "location": warehouse.location}
        return self.dao.insert(data)

    def update(self, warehouse: Warehouse) -> bool:
        """Update an existing warehouse.

        Args:
            warehouse: Warehouse model instance with ID.

        Returns:
            True if updated successfully.

        Raises:
            ValueError: If validation fails or ID is missing.
        """
        if warehouse.id is None:
            raise ValueError("Warehouse must have ID before update")
        warehouse.validate()
        data = {"id": warehouse.id, "name": warehouse.name, "location": warehouse.location}
        return self.dao.update(data)

    def delete(self, wh_id: int) -> bool:
        """Delete a warehouse.

        Args:
            wh_id: ID of the warehouse to delete.

        Returns:
            True if deleted successfully.

        Raises:
            ValueError: If ID is not an integer.
        """
        if not isinstance(wh_id, int):
            raise ValueError("ID must be int")
        return self.dao.delete(wh_id)

    def get_by_id(self, wh_id: int) -> Warehouse:
        """Get warehouse by ID.

        Args:
            wh_id: ID of the warehouse.

        Returns:
            Warehouse instance.

        Raises:
            ValueError: If ID is invalid or warehouse not found.
        """
        if not isinstance(wh_id, int):
            raise ValueError("ID must be int")
        data = self.dao.find_by_id(wh_id)
        if data is None:
            raise ValueError("Warehouse not found")
        return Warehouse(**data)

    def list_all(self) -> list[Warehouse]:
        """Get all warehouses as model instances.

        Returns:
            List of Warehouse instances.
        """
        dicts = self.dao.find_all()
        return [Warehouse(**d) for d in dicts]

    def get_stock_levels(self) -> list[dict]:
        """Get inventory stock levels across all warehouses.

        Returns:
            List of dictionaries with component, quantity, and unit information.
        """
        # TODO: Implement actual stock level aggregation from warehouse inventory
        # This should query components stored in warehouses
        # For now, return empty list as placeholder
        return []
```

---

## Backend - API

### `backend\app\api\__init__.py`

```python

```

### `backend\app\api\components.py`

```python
"""API endpoints for component management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.component_service import ComponentService
from ..dao.component_dao import ComponentDAO
from ..db.database import get_connection

router = APIRouter(prefix="/components", tags=["components"])


class ComponentCreate(BaseModel):
    """Schema for creating a component."""
    name: str
    unit: str
    qty: int = 0


class ComponentUpdate(BaseModel):
    """Schema for updating a component."""
    name: str
    unit: str
    qty: int


class ComponentResponse(BaseModel):
    """Schema for component response."""
    id: int
    name: str
    unit: str
    qty: int

    class Config:
        from_attributes = True


def get_component_service():
    """Dependency to get component service."""
    conn = get_connection()
    dao = ComponentDAO(conn)
    return ComponentService(dao)


@router.get("/", response_model=list[dict])
async def list_components(
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all components."""
    components = service.list_all()
    return components


@router.get("/{component_id}", response_model=dict)
async def get_component(
    component_id: int,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a component by ID."""
    try:
        component = service.get_by_id(component_id)
        return component
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
async def create_component(
    component: ComponentCreate,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new component."""
    try:
        component_id = service.create(component.model_dump())
        return {"id": component_id, "message": "Component created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{component_id}")
async def update_component(
    component_id: int,
    component: ComponentUpdate,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a component."""
    try:
        data = component.model_dump()
        success = service.update(component_id, data)
        if success:
            return {"message": "Component updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{component_id}")
async def delete_component(
    component_id: int,
    service: ComponentService = Depends(get_component_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a component."""
    try:
        success = service.delete(component_id)
        if success:
            return {"message": "Component deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### `backend\app\api\orders.py`

```python
"""API endpoints for order management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from ..core.auth import get_current_active_user
from ..services.order_service import OrderService
from ..dao.order_dao import OrderDAO
from ..db.database import get_connection

router = APIRouter(prefix="/orders", tags=["orders"])


class OrderCreate(BaseModel):
    """Schema for creating an order."""
    supplier: str
    status: str = "pending"


class OrderUpdate(BaseModel):
    """Schema for updating an order."""
    supplier: Optional[str] = None
    status: Optional[str] = None


class OrderResponse(BaseModel):
    """Schema for order response."""
    id: int
    order_id: Optional[int] = None
    supplier: str
    status: str
    date: Optional[str] = None

    class Config:
        from_attributes = True


def get_order_service():
    """Dependency to get order service."""
    conn = get_connection()
    dao = OrderDAO(conn)
    return OrderService(dao)


@router.get("/", response_model=list[dict])
async def list_orders(
    service: OrderService = Depends(get_order_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all orders."""
    orders = service.list_all()
    return orders


@router.post("/", response_model=dict)
async def create_order(
    order: OrderCreate,
    service: OrderService = Depends(get_order_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new order."""
    try:
        result = service.create(order.model_dump())
        return {"id": result.get("id"), "message": "Order created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{order_id}")
async def delete_order(
    order_id: int,
    service: OrderService = Depends(get_order_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete an order."""
    try:
        # Note: OrderService doesn't have delete, we'll call DAO directly
        service.order_dao.delete(order_id)
        return {"message": "Order deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### `backend\app\api\storekeepers.py`

```python
"""API endpoints for storekeeper management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.storekeeper_service import StorekeeperService
from ..dao.storekeeper_dao import StorekeeperDAO
from ..models.storekeeper import Storekeeper
from ..db.database import get_connection

router = APIRouter(prefix="/storekeepers", tags=["storekeepers"])


class StorekeeperCreate(BaseModel):
    """Schema for creating a storekeeper."""
    name: str
    warehouse_id: int


class StorekeeperUpdate(BaseModel):
    """Schema for updating a storekeeper."""
    name: str
    warehouse_id: int


class StorekeeperResponse(BaseModel):
    """Schema for storekeeper response."""
    id: int | None
    name: str
    warehouse_id: int

    class Config:
        from_attributes = True


def get_storekeeper_service():
    """Dependency to get storekeeper service."""
    conn = get_connection()
    dao = StorekeeperDAO(conn)
    return StorekeeperService(dao)


@router.get("/", response_model=list[StorekeeperResponse])
async def list_storekeepers(
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all storekeepers."""
    storekeepers = service.list_all()
    return storekeepers


@router.get("/{storekeeper_id}", response_model=StorekeeperResponse)
async def get_storekeeper(
    storekeeper_id: int,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a storekeeper by ID."""
    try:
        storekeeper = service.get_by_id(storekeeper_id)
        return storekeeper
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
async def create_storekeeper(
    storekeeper: StorekeeperCreate,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new storekeeper."""
    try:
        sk = Storekeeper(name=storekeeper.name, warehouse_id=storekeeper.warehouse_id)
        storekeeper_id = service.create(sk)
        return {"id": storekeeper_id, "message": "Storekeeper created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{storekeeper_id}")
async def update_storekeeper(
    storekeeper_id: int,
    storekeeper: StorekeeperUpdate,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a storekeeper."""
    try:
        sk = Storekeeper(id=storekeeper_id, name=storekeeper.name, warehouse_id=storekeeper.warehouse_id)
        success = service.update(sk)
        if success:
            return {"message": "Storekeeper updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{storekeeper_id}")
async def delete_storekeeper(
    storekeeper_id: int,
    service: StorekeeperService = Depends(get_storekeeper_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a storekeeper."""
    try:
        success = service.delete(storekeeper_id)
        if success:
            return {"message": "Storekeeper deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### `backend\app\api\suppliers.py`

```python
"""API endpoints for supplier management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.supplier_service import SupplierService
from ..dao.supplier_dao import SupplierDAO
from ..db.database import get_connection

router = APIRouter(prefix="/suppliers", tags=["suppliers"])


class SupplierCreate(BaseModel):
    """Schema for creating a supplier."""
    name: str
    contact_info: str = ""


class SupplierUpdate(BaseModel):
    """Schema for updating a supplier."""
    name: str
    contact_info: str = ""


class SupplierResponse(BaseModel):
    """Schema for supplier response."""
    id: int
    name: str
    contact_info: str

    class Config:
        from_attributes = True


def get_supplier_service():
    """Dependency to get supplier service."""
    conn = get_connection()
    dao = SupplierDAO(conn)
    return SupplierService(dao)


@router.get("/", response_model=list[SupplierResponse])
async def list_suppliers(
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all suppliers."""
    suppliers = service.list_all()
    return suppliers


@router.get("/{supplier_id}", response_model=SupplierResponse)
async def get_supplier(
    supplier_id: int,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a supplier by ID."""
    try:
        supplier = service.get_by_id(supplier_id)
        return supplier
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
async def create_supplier(
    supplier: SupplierCreate,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new supplier."""
    try:
        supplier_id = service.create(supplier.model_dump())
        return {"id": supplier_id, "message": "Supplier created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{supplier_id}")
async def update_supplier(
    supplier_id: int,
    supplier: SupplierUpdate,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a supplier."""
    try:
        data = supplier.model_dump()
        data["id"] = supplier_id
        success = service.update(data)
        if success:
            return {"message": "Supplier updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{supplier_id}")
async def delete_supplier(
    supplier_id: int,
    service: SupplierService = Depends(get_supplier_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a supplier."""
    try:
        success = service.delete(supplier_id)
        if success:
            return {"message": "Supplier deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### `backend\app\api\supplies.py`

```python
"""API endpoints for supply management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

from ..core.auth import get_current_active_user
from ..services.supply_service import SupplyService
from ..dao.supply_dao import SupplyDAO
from ..dao.supply_record_dao import SupplyRecordDAO
from ..services.inventory_observer import InventoryObserver
from ..dao.component_dao import ComponentDAO
from ..db.database import get_connection

router = APIRouter(prefix="/supplies", tags=["supplies"])


class SupplyCreate(BaseModel):
    """Schema for creating a supply."""
    supplier_id: int
    date: Optional[str] = None


class SupplyResponse(BaseModel):
    """Schema for supply response."""
    id: int
    supplier_id: int
    date: Optional[str] = None

    class Config:
        from_attributes = True


def get_supply_service():
    """Dependency to get supply service."""
    conn = get_connection()
    supply_dao = SupplyDAO(conn)
    component_dao = ComponentDAO(conn)
    inventory_observer = InventoryObserver(component_dao)
    supply_record_dao = SupplyRecordDAO(conn, inventory_observer)
    return SupplyService(supply_dao, supply_record_dao)


@router.get("/", response_model=list[dict])
async def list_supplies(
    service: SupplyService = Depends(get_supply_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all supplies."""
    supplies = service.list_all()
    return supplies


@router.post("/", response_model=dict)
async def create_supply(
    supply: SupplyCreate,
    service: SupplyService = Depends(get_supply_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new supply."""
    try:
        supply_id = service.create(supply.model_dump())
        return {"id": supply_id, "message": "Supply created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{supply_id}")
async def delete_supply(
    supply_id: int,
    service: SupplyService = Depends(get_supply_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a supply."""
    try:
        success = service.delete(supply_id)
        if success:
            return {"message": "Supply deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### `backend\app\api\warehouses.py`

```python
"""API endpoints for warehouse management."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..core.auth import get_current_active_user
from ..services.warehouse_service import WarehouseService
from ..dao.warehouse_dao import WarehouseDAO
from ..models.warehouse import Warehouse
from ..db.database import get_connection

router = APIRouter(prefix="/warehouses", tags=["warehouses"])


class WarehouseCreate(BaseModel):
    """Schema for creating a warehouse."""
    name: str
    location: str = ""


class WarehouseUpdate(BaseModel):
    """Schema for updating a warehouse."""
    name: str
    location: str = ""


class WarehouseResponse(BaseModel):
    """Schema for warehouse response."""
    id: int | None
    name: str
    location: str

    class Config:
        from_attributes = True


def get_warehouse_service():
    """Dependency to get warehouse service."""
    conn = get_connection()
    dao = WarehouseDAO(conn)
    return WarehouseService(dao)


@router.get("/", response_model=list[WarehouseResponse])
async def list_warehouses(
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all warehouses."""
    warehouses = service.list_all()
    return warehouses


@router.get("/stock-levels", response_model=list[dict])
async def get_stock_levels(
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get inventory stock levels across all warehouses."""
    stock_data = service.get_stock_levels()
    return stock_data


@router.get("/{warehouse_id}", response_model=WarehouseResponse)
async def get_warehouse(
    warehouse_id: int,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Get a warehouse by ID."""
    try:
        warehouse = service.get_by_id(warehouse_id)
        return warehouse
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
async def create_warehouse(
    warehouse: WarehouseCreate,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Create a new warehouse."""
    try:
        wh = Warehouse(name=warehouse.name, location=warehouse.location)
        warehouse_id = service.create(wh)
        return {"id": warehouse_id, "message": "Warehouse created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{warehouse_id}")
async def update_warehouse(
    warehouse_id: int,
    warehouse: WarehouseUpdate,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Update a warehouse."""
    try:
        wh = Warehouse(id=warehouse_id, name=warehouse.name, location=warehouse.location)
        success = service.update(wh)
        if success:
            return {"message": "Warehouse updated successfully"}
        raise HTTPException(status_code=400, detail="Update failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{warehouse_id}")
async def delete_warehouse(
    warehouse_id: int,
    service: WarehouseService = Depends(get_warehouse_service),
    current_user: dict = Depends(get_current_active_user)
):
    """Delete a warehouse."""
    try:
        success = service.delete(warehouse_id)
        if success:
            return {"message": "Warehouse deleted successfully"}
        raise HTTPException(status_code=400, detail="Delete failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

## Frontend - Config

### `frontend\index.html`

```html
<!doctype html>
<html lang="uk">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ІС відділу комплектації</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

### `frontend\package.json`

```json
{
  "name": "supply-management-frontend",
  "private": true,
  "version": "2.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.1",
    "axios": "^1.6.5",
    "react-hot-toast": "^2.4.1"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32",
    "tailwindcss": "^3.4.0",
    "vite": "^5.0.8"
  }
}
```

### `frontend\postcss.config.js`

```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

### `frontend\README.md`

```markdown
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
```

### `frontend\src\App.jsx`

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import Layout from './components/Layout/Layout';
import Dashboard from './pages/Dashboard';
import SuppliersPage from './pages/SuppliersPage';
import ComponentsPage from './pages/ComponentsPage';
import WarehousesPage from './pages/WarehousesPage';
import OrdersPage from './pages/OrdersPage';
import StorekeepersPage from './pages/StorekeepersPage';
import SuppliesPage from './pages/SuppliesPage';

function App() {
  return (
    <BrowserRouter>
      <Toaster />
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="suppliers" element={<SuppliersPage />} />
          <Route path="components" element={<ComponentsPage />} />
          <Route path="warehouses" element={<WarehousesPage />} />
          <Route path="orders" element={<OrdersPage />} />
          <Route path="storekeepers" element={<StorekeepersPage />} />
          <Route path="supplies" element={<SuppliesPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### `frontend\src\index.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply bg-primary-600 hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200;
  }

  .btn-secondary {
    @apply bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-4 rounded-lg transition-colors duration-200;
  }

  .btn-danger {
    @apply bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200;
  }

  .input-field {
    @apply w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent;
  }

  .card {
    @apply bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200;
  }
}
```

### `frontend\src\main.jsx`

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
```

### `frontend\tailwind.config.js`

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        }
      }
    },
  },
  plugins: [],
}
```

### `frontend\vite.config.js`

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
})
```

---

## Frontend - Services

### `frontend\src\services\api.js`

```javascript
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  // Basic auth credentials
  auth: {
    username: 'admin',
    password: 'admin'
  }
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // You can add authorization headers here
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Handle errors globally
    if (error.response) {
      console.error('API Error:', error.response.data);
    }
    return Promise.reject(error);
  }
);

export default api;
```

### `frontend\src\services\ordersService.js`

```javascript
import api from './api';

export const ordersService = {
  // Get all orders
  getAll: async () => {
    const response = await api.get('/orders/');
    return response.data;
  },

  // Create new order
  create: async (data) => {
    const response = await api.post('/orders/', data);
    return response.data;
  },

  // Delete order
  delete: async (id) => {
    const response = await api.delete(`/orders/${id}`);
    return response.data;
  }
};
```

### `frontend\src\services\storekeepersService.js`

```javascript
import api from './api';

export const storekeepersService = {
  // Get all storekeepers
  getAll: async () => {
    const response = await api.get('/storekeepers/');
    return response.data;
  },

  // Get storekeeper by ID
  getById: async (id) => {
    const response = await api.get(`/storekeepers/${id}`);
    return response.data;
  },

  // Create new storekeeper
  create: async (data) => {
    const response = await api.post('/storekeepers/', data);
    return response.data;
  },

  // Update storekeeper
  update: async (id, data) => {
    const response = await api.put(`/storekeepers/${id}`, data);
    return response.data;
  },

  // Delete storekeeper
  delete: async (id) => {
    const response = await api.delete(`/storekeepers/${id}`);
    return response.data;
  }
};
```

### `frontend\src\services\suppliersService.js`

```javascript
import api from './api';

export const suppliersService = {
  // Get all suppliers
  getAll: async () => {
    const response = await api.get('/suppliers/');
    return response.data;
  },

  // Get supplier by ID
  getById: async (id) => {
    const response = await api.get(`/suppliers/${id}`);
    return response.data;
  },

  // Create new supplier
  create: async (data) => {
    const response = await api.post('/suppliers/', data);
    return response.data;
  },

  // Update supplier
  update: async (id, data) => {
    const response = await api.put(`/suppliers/${id}`, data);
    return response.data;
  },

  // Delete supplier
  delete: async (id) => {
    const response = await api.delete(`/suppliers/${id}`);
    return response.data;
  }
};
```

### `frontend\src\services\suppliesService.js`

```javascript
import api from './api';

export const suppliesService = {
  // Get all supplies
  getAll: async () => {
    const response = await api.get('/supplies/');
    return response.data;
  },

  // Create new supply
  create: async (data) => {
    const response = await api.post('/supplies/', data);
    return response.data;
  },

  // Delete supply
  delete: async (id) => {
    const response = await api.delete(`/supplies/${id}`);
    return response.data;
  }
};
```

### `frontend\src\services\warehousesService.js`

```javascript
import api from './api';

export const warehousesService = {
  // Get all warehouses
  getAll: async () => {
    const response = await api.get('/warehouses/');
    return response.data;
  },

  // Get stock levels
  getStockLevels: async () => {
    const response = await api.get('/warehouses/stock-levels');
    return response.data;
  },

  // Get warehouse by ID
  getById: async (id) => {
    const response = await api.get(`/warehouses/${id}`);
    return response.data;
  },

  // Create new warehouse
  create: async (data) => {
    const response = await api.post('/warehouses/', data);
    return response.data;
  },

  // Update warehouse
  update: async (id, data) => {
    const response = await api.put(`/warehouses/${id}`, data);
    return response.data;
  },

  // Delete warehouse
  delete: async (id) => {
    const response = await api.delete(`/warehouses/${id}`);
    return response.data;
  }
};
```

---

## Frontend - Hooks

### `frontend\src\hooks\useToast.js`

```javascript
import toast from 'react-hot-toast';

export const useToast = () => {
  return {
    success: (message) => toast.success(message, {
      duration: 3000,
      position: 'top-right',
      style: {
        background: '#10B981',
        color: '#fff',
      },
    }),

    error: (message) => toast.error(message, {
      duration: 4000,
      position: 'top-right',
      style: {
        background: '#EF4444',
        color: '#fff',
      },
    }),

    loading: (message) => toast.loading(message, {
      position: 'top-right',
    }),

    promise: (promise, messages) => toast.promise(promise, messages, {
      position: 'top-right',
    }),

    custom: (message, options) => toast(message, options),

    dismiss: (toastId) => toast.dismiss(toastId),
  };
};
```

---

## Frontend - Pages

### `frontend\src\pages\ComponentsPage.jsx`

```jsx
import ComponentsList from '../components/Components/ComponentsList';

export default function ComponentsPage() {
  return <ComponentsList />;
}
```

### `frontend\src\pages\Dashboard.jsx`

```jsx
import { useState, useEffect } from 'react';
import { suppliersService } from '../services/suppliersService';
import { componentsService } from '../services/componentsService';
import { warehousesService } from '../services/warehousesService';
import { Link } from 'react-router-dom';

export default function Dashboard() {
  const [stats, setStats] = useState({
    suppliers: 0,
    components: 0,
    warehouses: 0,
    lowStock: 0
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const [suppliers, components, warehouses] = await Promise.all([
        suppliersService.getAll(),
        componentsService.getAll(),
        warehousesService.getAll()
      ]);

      const lowStock = components.filter(c => c.qty < 50).length;

      setStats({
        suppliers: suppliers.length,
        components: components.length,
        warehouses: warehouses.length,
        lowStock
      });
    } catch (err) {
      console.error('Error loading stats:', err);
    } finally {
      setLoading(false);
    }
  };

  const statCards = [
    { title: 'Постачальники', value: stats.suppliers, icon: '🏢', link: '/suppliers', color: 'bg-blue-500' },
    { title: 'Комплектуючі', value: stats.components, icon: '🔧', link: '/components', color: 'bg-green-500' },
    { title: 'Склади', value: stats.warehouses, icon: '🏭', link: '/warehouses', color: 'bg-purple-500' },
    { title: 'Низький запас', value: stats.lowStock, icon: '⚠️', link: '/components', color: 'bg-yellow-500' },
  ];

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-gray-600">Завантаження...</div>
      </div>
    );
  }

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Дашборд</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {statCards.map((stat) => (
          <Link
            key={stat.title}
            to={stat.link}
            className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-6"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 mb-1">{stat.title}</p>
                <p className="text-3xl font-bold text-gray-900">{stat.value}</p>
              </div>
              <div className={`${stat.color} w-12 h-12 rounded-lg flex items-center justify-center text-2xl`}>
                {stat.icon}
              </div>
            </div>
          </Link>
        ))}
      </div>

      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold mb-4">Швидкі дії</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Link to="/suppliers" className="btn-primary text-center">
            Керувати постачальниками
          </Link>
          <Link to="/components" className="btn-primary text-center">
            Керувати комплектуючими
          </Link>
          <Link to="/warehouses" className="btn-primary text-center">
            Керувати складами
          </Link>
        </div>
      </div>
    </div>
  );
}
```

### `frontend\src\pages\OrdersPage.jsx`

```jsx
import OrdersList from '../components/Orders/OrdersList';

export default function OrdersPage() {
  return <OrdersList />;
}
```

### `frontend\src\pages\StorekeepersPage.jsx`

```jsx
import StorekeepersList from '../components/Storekeepers/StorekeepersList';

export default function StorekeepersPage() {
  return <StorekeepersList />;
}
```

### `frontend\src\pages\SuppliersPage.jsx`

```jsx
import SuppliersList from '../components/Suppliers/SuppliersList';

export default function SuppliersPage() {
  return <SuppliersList />;
}
```

### `frontend\src\pages\SuppliesPage.jsx`

```jsx
import SuppliesList from '../components/Supplies/SuppliesList';

export default function SuppliesPage() {
  return <SuppliesList />;
}
```

### `frontend\src\pages\WarehousesPage.jsx`

```jsx
import WarehousesList from '../components/Warehouses/WarehousesList';

export default function WarehousesPage() {
  return <WarehousesList />;
}
```

---

## Frontend - Components

### `frontend\src\components\Components\ComponentCard.jsx`

```jsx
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
```

### `frontend\src\components\Components\ComponentForm.jsx`

```jsx
import { useState, useEffect } from 'react';

export default function ComponentForm({ component, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    unit: 'шт',
    qty: 0
  });

  useEffect(() => {
    if (component) {
      setFormData({
        name: component.name,
        unit: component.unit || 'шт',
        qty: component.qty || 0
      });
    }
  }, [component]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'qty' ? parseInt(value) || 0 : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.name.trim()) {
      alert('Будь ласка, введіть назву комплектуючого');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">
        {component ? 'Редагувати комплектуюче' : 'Нове комплектуюче'}
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
              placeholder="Введіть назву комплектуючого"
              required
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Одиниця виміру
              </label>
              <select
                name="unit"
                value={formData.unit}
                onChange={handleChange}
                className="input-field"
              >
                <option value="шт">шт (штуки)</option>
                <option value="кг">кг (кілограми)</option>
                <option value="м">м (метри)</option>
                <option value="л">л (літри)</option>
                <option value="пач">пач (пачки)</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Кількість
              </label>
              <input
                type="number"
                name="qty"
                value={formData.qty}
                onChange={handleChange}
                className="input-field"
                min="0"
              />
            </div>
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            {component ? 'Зберегти' : 'Створити'}
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
```

### `frontend\src\components\Components\ComponentsList.jsx`

```jsx
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
```

### `frontend\src\components\Layout\Header.jsx`

```jsx
export default function Header() {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <h1 className="text-2xl font-bold text-primary-600">
              ІС відділу комплектації
            </h1>
          </div>
          <div className="flex items-center space-x-4">
            <span className="text-sm text-gray-600">
              👤 Admin
            </span>
          </div>
        </div>
      </div>
    </header>
  );
}
```

### `frontend\src\components\Layout\Layout.jsx`

```jsx
import { Outlet } from 'react-router-dom';
import Header from './Header';
import Sidebar from './Sidebar';

export default function Layout() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      <div className="flex">
        <Sidebar />
        <main className="flex-1 md:ml-64 pt-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  );
}
```

### `frontend\src\components\Layout\Sidebar.jsx`

```jsx
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
```

### `frontend\src\components\Orders\OrderCard.jsx`

```jsx
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
```

### `frontend\src\components\Orders\OrderForm.jsx`

```jsx
import { useState } from 'react';

export default function OrderForm({ onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    supplier: '',
    status: 'pending'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.supplier.trim()) {
      alert('Будь ласка, введіть постачальника');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">Нове замовлення</h3>

      <form onSubmit={handleSubmit}>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Постачальник <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              name="supplier"
              value={formData.supplier}
              onChange={handleChange}
              className="input-field"
              placeholder="Введіть назву постачальника"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Статус
            </label>
            <select
              name="status"
              value={formData.status}
              onChange={handleChange}
              className="input-field"
            >
              <option value="pending">Очікує</option>
              <option value="confirmed">Підтверджено</option>
              <option value="delivered">Доставлено</option>
              <option value="cancelled">Скасовано</option>
            </select>
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            Створити
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
```

### `frontend\src\components\Orders\OrdersList.jsx`

```jsx
import { useState, useEffect } from 'react';
import { ordersService } from '../../services/ordersService';
import { useToast } from '../../hooks/useToast';
import OrderCard from './OrderCard';
import OrderForm from './OrderForm';

export default function OrdersList() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const toast = useToast();

  useEffect(() => {
    loadOrders();
  }, []);

  const loadOrders = async () => {
    try {
      setLoading(true);
      const data = await ordersService.getAll();
      setOrders(data);
    } catch (err) {
      toast.error('Не вдалося завантажити замовлення');
      console.error('Error loading orders:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити це замовлення?')) {
      return;
    }

    try {
      await ordersService.delete(id);
      toast.success('Замовлення видалено');
      loadOrders();
    } catch (err) {
      toast.error('Не вдалося видалити замовлення');
      console.error('Error deleting order:', err);
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      await ordersService.create(data);
      toast.success('Замовлення створено');
      setShowForm(false);
      loadOrders();
    } catch (err) {
      toast.error('Не вдалося створити замовлення');
      console.error('Error creating order:', err);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-gray-600">Завантаження...</div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-900">Замовлення</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Створити замовлення
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <OrderForm
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {orders.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає замовлень</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {orders.map((order) => (
            <OrderCard
              key={order.id}
              order={order}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
```

### `frontend\src\components\Storekeepers\StorekeeperCard.jsx`

```jsx
export default function StorekeeperCard({ storekeeper, warehouses, onEdit, onDelete }) {
  const warehouse = warehouses.find(w => w.id === storekeeper.warehouse_id);

  return (
    <div className="card p-4">
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-lg font-semibold text-gray-900">{storekeeper.name}</h3>
        <span className="text-xs text-gray-500">#{storekeeper.id}</span>
      </div>

      <div className="mb-4">
        <p className="text-sm text-gray-600">
          🏭 Склад: {warehouse ? warehouse.name : 'Не призначено'}
        </p>
        {warehouse && warehouse.location && (
          <p className="text-xs text-gray-500 mt-1">
            📍 {warehouse.location}
          </p>
        )}
      </div>

      <div className="flex space-x-2">
        <button
          onClick={() => onEdit(storekeeper)}
          className="flex-1 bg-primary-50 text-primary-700 hover:bg-primary-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Редагувати
        </button>
        <button
          onClick={() => onDelete(storekeeper.id)}
          className="flex-1 bg-red-50 text-red-700 hover:bg-red-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Видалити
        </button>
      </div>
    </div>
  );
}
```

### `frontend\src\components\Storekeepers\StorekeeperForm.jsx`

```jsx
import { useState, useEffect } from 'react';

export default function StorekeeperForm({ storekeeper, warehouses, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    warehouse_id: ''
  });

  useEffect(() => {
    if (storekeeper) {
      setFormData({
        name: storekeeper.name,
        warehouse_id: storekeeper.warehouse_id
      });
    }
  }, [storekeeper]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'warehouse_id' ? parseInt(value) : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.name.trim()) {
      alert("Будь ласка, введіть ім'я комірника");
      return;
    }
    if (!formData.warehouse_id) {
      alert('Будь ласка, виберіть склад');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">
        {storekeeper ? 'Редагувати комірника' : 'Новий комірник'}
      </h3>

      <form onSubmit={handleSubmit}>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Ім'я <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="input-field"
              placeholder="Введіть ім'я комірника"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Склад <span className="text-red-500">*</span>
            </label>
            <select
              name="warehouse_id"
              value={formData.warehouse_id}
              onChange={handleChange}
              className="input-field"
              required
            >
              <option value="">Виберіть склад</option>
              {warehouses.map((warehouse) => (
                <option key={warehouse.id} value={warehouse.id}>
                  {warehouse.name} {warehouse.location && `(${warehouse.location})`}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            {storekeeper ? 'Зберегти' : 'Створити'}
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
```

### `frontend\src\components\Storekeepers\StorekeepersList.jsx`

```jsx
import { useState, useEffect } from 'react';
import { storekeepersService } from '../../services/storekeepersService';
import { warehousesService } from '../../services/warehousesService';
import { useToast } from '../../hooks/useToast';
import StorekeeperCard from './StorekeeperCard';
import StorekeeperForm from './StorekeeperForm';

export default function StorekeepersList() {
  const [storekeepers, setStorekeepers] = useState([]);
  const [warehouses, setWarehouses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingStorekeeper, setEditingStorekeeper] = useState(null);
  const toast = useToast();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [storekeepersData, warehousesData] = await Promise.all([
        storekeepersService.getAll(),
        warehousesService.getAll()
      ]);
      setStorekeepers(storekeepersData);
      setWarehouses(warehousesData);
    } catch (err) {
      toast.error('Не вдалося завантажити дані');
      console.error('Error loading data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingStorekeeper(null);
    setShowForm(true);
  };

  const handleEdit = (storekeeper) => {
    setEditingStorekeeper(storekeeper);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цього комірника?')) {
      return;
    }

    try {
      await storekeepersService.delete(id);
      toast.success('Комірника видалено');
      loadData();
    } catch (err) {
      toast.error('Не вдалося видалити комірника');
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingStorekeeper) {
        await storekeepersService.update(editingStorekeeper.id, data);
        toast.success('Комірника оновлено');
      } else {
        await storekeepersService.create(data);
        toast.success('Комірника створено');
      }
      setShowForm(false);
      loadData();
    } catch (err) {
      toast.error('Не вдалося зберегти комірника');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-gray-600">Завантаження...</div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-900">Комірники</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Додати комірника
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <StorekeeperForm
            storekeeper={editingStorekeeper}
            warehouses={warehouses}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {storekeepers.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає комірників</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {storekeepers.map((storekeeper) => (
            <StorekeeperCard
              key={storekeeper.id}
              storekeeper={storekeeper}
              warehouses={warehouses}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
```

### `frontend\src\components\Suppliers\SupplierCard.jsx`

```jsx
export default function SupplierCard({ supplier, onEdit, onDelete }) {
  return (
    <div className="card p-4">
      <div className="flex justify-between items-start mb-2">
        <h3 className="text-lg font-semibold text-gray-900">{supplier.name}</h3>
        <span className="text-xs text-gray-500">#{supplier.id}</span>
      </div>

      <div className="mb-4">
        <p className="text-sm text-gray-600">
          📞 {supplier.contact_info || 'Немає контактної інформації'}
        </p>
      </div>

      <div className="flex space-x-2">
        <button
          onClick={() => onEdit(supplier)}
          className="flex-1 bg-primary-50 text-primary-700 hover:bg-primary-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Редагувати
        </button>
        <button
          onClick={() => onDelete(supplier.id)}
          className="flex-1 bg-red-50 text-red-700 hover:bg-red-100 py-2 px-3 rounded-md text-sm font-medium transition-colors"
        >
          Видалити
        </button>
      </div>
    </div>
  );
}
```

### `frontend\src\components\Suppliers\SupplierForm.jsx`

```jsx
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
```

### `frontend\src\components\Suppliers\SuppliersList.jsx`

```jsx
import { useState, useEffect } from 'react';
import { suppliersService } from '../../services/suppliersService';
import SupplierCard from './SupplierCard';
import SupplierForm from './SupplierForm';

export default function SuppliersList() {
  const [suppliers, setSuppliers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingSupplier, setEditingSupplier] = useState(null);

  useEffect(() => {
    loadSuppliers();
  }, []);

  const loadSuppliers = async () => {
    try {
      setLoading(true);
      const data = await suppliersService.getAll();
      setSuppliers(data);
      setError(null);
    } catch (err) {
      setError('Не вдалося завантажити постачальників');
      console.error('Error loading suppliers:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingSupplier(null);
    setShowForm(true);
  };

  const handleEdit = (supplier) => {
    setEditingSupplier(supplier);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цього постачальника?')) {
      return;
    }

    try {
      await suppliersService.delete(id);
      loadSuppliers();
    } catch (err) {
      alert('Не вдалося видалити постачальника');
      console.error('Error deleting supplier:', err);
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingSupplier) {
        await suppliersService.update(editingSupplier.id, data);
      } else {
        await suppliersService.create(data);
      }
      setShowForm(false);
      loadSuppliers();
    } catch (err) {
      alert('Не вдалося зберегти постачальника');
      console.error('Error saving supplier:', err);
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
        <h2 className="text-2xl font-bold text-gray-900">Постачальники</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Додати постачальника
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <SupplierForm
            supplier={editingSupplier}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {suppliers.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає постачальників</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {suppliers.map((supplier) => (
            <SupplierCard
              key={supplier.id}
              supplier={supplier}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
```

### `frontend\src\components\Supplies\SuppliesList.jsx`

```jsx
import { useState, useEffect } from 'react';
import { suppliesService } from '../../services/suppliesService';
import { suppliersService } from '../../services/suppliersService';
import { useToast } from '../../hooks/useToast';
import SupplyCard from './SupplyCard';
import SupplyForm from './SupplyForm';

export default function SuppliesList() {
  const [supplies, setSupplies] = useState([]);
  const [suppliers, setSuppliers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const toast = useToast();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [suppliesData, suppliersData] = await Promise.all([
        suppliesService.getAll(),
        suppliersService.getAll()
      ]);
      setSupplies(suppliesData);
      setSuppliers(suppliersData);
    } catch (err) {
      toast.error('Не вдалося завантажити дані');
      console.error('Error loading data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цю поставку?')) {
      return;
    }

    try {
      await suppliesService.delete(id);
      toast.success('Поставку видалено');
      loadData();
    } catch (err) {
      toast.error('Не вдалося видалити поставку');
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      await suppliesService.create(data);
      toast.success('Поставку зареєстровано');
      setShowForm(false);
      loadData();
    } catch (err) {
      toast.error('Не вдалося зареєструвати поставку');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-lg text-gray-600">Завантаження...</div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-900">Поставки</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Зареєструвати поставку
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <SupplyForm
            suppliers={suppliers}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {supplies.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає поставок</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {supplies.map((supply) => (
            <SupplyCard
              key={supply.id}
              supply={supply}
              suppliers={suppliers}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
```

### `frontend\src\components\Supplies\SupplyCard.jsx`

```jsx
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
```

### `frontend\src\components\Supplies\SupplyForm.jsx`

```jsx
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
```

### `frontend\src\components\Warehouses\WarehouseCard.jsx`

```jsx
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
```

### `frontend\src\components\Warehouses\WarehouseForm.jsx`

```jsx
import { useState, useEffect } from 'react';

export default function WarehouseForm({ warehouse, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    location: ''
  });

  useEffect(() => {
    if (warehouse) {
      setFormData({
        name: warehouse.name,
        location: warehouse.location || ''
      });
    }
  }, [warehouse]);

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
      alert('Будь ласка, введіть назву складу');
      return;
    }
    onSubmit(formData);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold mb-4">
        {warehouse ? 'Редагувати склад' : 'Новий склад'}
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
              placeholder="Введіть назву складу"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Локація
            </label>
            <input
              type="text"
              name="location"
              value={formData.location}
              onChange={handleChange}
              className="input-field"
              placeholder="Адреса або опис розташування..."
            />
          </div>
        </div>

        <div className="flex space-x-3 mt-6">
          <button type="submit" className="btn-primary flex-1">
            {warehouse ? 'Зберегти' : 'Створити'}
          </button>
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Скасувати
          </button>
        </div>
      </form>
    </div>
  );
}
```

### `frontend\src\components\Warehouses\WarehousesList.jsx`

```jsx
import { useState, useEffect } from 'react';
import { warehousesService } from '../../services/warehousesService';
import WarehouseCard from './WarehouseCard';
import WarehouseForm from './WarehouseForm';

export default function WarehousesList() {
  const [warehouses, setWarehouses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingWarehouse, setEditingWarehouse] = useState(null);

  useEffect(() => {
    loadWarehouses();
  }, []);

  const loadWarehouses = async () => {
    try {
      setLoading(true);
      const data = await warehousesService.getAll();
      setWarehouses(data);
      setError(null);
    } catch (err) {
      setError('Не вдалося завантажити склади');
      console.error('Error loading warehouses:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = () => {
    setEditingWarehouse(null);
    setShowForm(true);
  };

  const handleEdit = (warehouse) => {
    setEditingWarehouse(warehouse);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Ви впевнені, що хочете видалити цей склад?')) {
      return;
    }

    try {
      await warehousesService.delete(id);
      loadWarehouses();
    } catch (err) {
      alert('Не вдалося видалити склад');
      console.error('Error deleting warehouse:', err);
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingWarehouse) {
        await warehousesService.update(editingWarehouse.id, data);
      } else {
        await warehousesService.create(data);
      }
      setShowForm(false);
      loadWarehouses();
    } catch (err) {
      alert('Не вдалося зберегти склад');
      console.error('Error saving warehouse:', err);
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
        <h2 className="text-2xl font-bold text-gray-900">Склади</h2>
        <button onClick={handleCreate} className="btn-primary">
          + Додати склад
        </button>
      </div>

      {showForm && (
        <div className="mb-6">
          <WarehouseForm
            warehouse={editingWarehouse}
            onSubmit={handleFormSubmit}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {warehouses.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-500">Немає складів</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {warehouses.map((warehouse) => (
            <WarehouseCard
              key={warehouse.id}
              warehouse={warehouse}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}
```

### `frontend\src\services\componentsService.js`

```javascript
import api from './api';

export const componentsService = {
  // Get all components
  getAll: async () => {
    const response = await api.get('/components/');
    return response.data;
  },

  // Get component by ID
  getById: async (id) => {
    const response = await api.get(`/components/${id}`);
    return response.data;
  },

  // Create new component
  create: async (data) => {
    const response = await api.post('/components/', data);
    return response.data;
  },

  // Update component
  update: async (id, data) => {
    const response = await api.put(`/components/${id}`, data);
    return response.data;
  },

  // Delete component
  delete: async (id) => {
    const response = await api.delete(`/components/${id}`);
    return response.data;
  }
};
```

---

## Tests

### `tests\__init__.py`

```python

```

### `tests\conftest.py`

```python
import pytest
from dao.component_dao import ComponentDAO
from db.database import get_connection


@pytest.fixture
def component_dao(tmp_path):
    return ComponentDAO(get_connection(tmp_path / "t.db"))


@pytest.fixture
def sample_component():
    return {"name": "Bolt", "unit": "pcs", "quantity_in_stock": 100}
```

### `tests\dao\__init__.py`

```python

```

### `tests\dao\test_component_dao.py`

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from db.database import get_connection
from dao.component_dao import ComponentDAO


@pytest.fixture
def dao():
    conn = get_connection(':memory:')
    return ComponentDAO(conn)


@pytest.fixture
def component_dao():
    conn = get_connection(':memory:')
    return ComponentDAO(conn)


@pytest.fixture
def sample_component():
    return {"name": "Bolt", "unit": "pcs", "quantity_in_stock": 10}


def test_insert_and_select(component_dao, sample_component):
    """Test inserting and selecting component."""
    cid = component_dao.insert(sample_component)
    assert cid > 0

    stored = component_dao.find_by_id(cid)
    assert stored is not None
    assert stored["name"] == sample_component["name"]
    assert stored["quantity_in_stock"] == sample_component["quantity_in_stock"]


def test_update_quantity(dao):
    """Test updating component quantity."""
    data = {"name": "Nut", "unit": "pcs", "quantity_in_stock": 5}
    comp_id = dao.insert(data)

    dao.update_quantity(comp_id, 3)

    updated = dao.find_by_id(comp_id)
    assert updated["quantity_in_stock"] == 8
```

### `tests\dao\test_storekeeper_dao.py`

```python
import sqlite3
import pytest
from dao.storekeeper_dao import StorekeeperDAO
from dao.warehouse_dao import WarehouseDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Create warehouse table for foreign key
    WarehouseDAO(conn).insert({"name": "W1", "location": "X"})
    return StorekeeperDAO(conn)


def test_insert_and_find_by_id(dao):
    """Test inserting and finding storekeeper by ID."""
    data = {"name": "Ivan", "warehouse_id": 1}
    k_id = dao.insert(data)
    assert k_id > 0

    found = dao.find_by_id(k_id)
    assert found is not None
    assert found["name"] == "Ivan"
    assert found["warehouse_id"] == 1


def test_update_and_find_all(dao):
    """Test updating storekeeper and retrieving all."""
    data = {"name": "Ivan", "warehouse_id": 1}
    k_id = dao.insert(data)

    # Update
    update_data = {"id": k_id, "name": "Stepan", "warehouse_id": 1}
    dao.update(update_data)

    all_k = dao.find_all()
    assert any(x["name"] == "Stepan" for x in all_k)


def test_delete(dao):
    """Test deleting a storekeeper."""
    data = {"name": "Petro", "warehouse_id": 1}
    k_id = dao.insert(data)

    assert dao.delete(k_id)
    assert dao.find_by_id(k_id) is None
```

### `tests\dao\test_supplier_dao.py`

```python
import sqlite3
import pytest
from dao.supplier_dao import SupplierDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    return SupplierDAO(conn)


def test_insert_and_find_by_id(dao):
    """Test inserting and finding supplier by ID."""
    data = {"name": "Sigma", "contact_info": "sig@mail.com"}
    s_id = dao.insert(data)
    assert s_id > 0

    found = dao.find_by_id(s_id)
    assert found is not None
    assert found["name"] == "Sigma"
    assert found["contact_info"] == "sig@mail.com"


def test_update_and_find_all(dao):
    """Test updating supplier and retrieving all."""
    data = {"name": "Beta", "contact_info": "b@b.com"}
    s_id = dao.insert(data)

    # Update
    update_data = {"id": s_id, "name": "Alpha", "contact_info": "b@b.com"}
    dao.update(update_data)

    all_s = dao.find_all()
    assert any(x["name"] == "Alpha" for x in all_s)


def test_delete(dao):
    """Test deleting a supplier."""
    data = {"name": "ToDelete", "contact_info": "none"}
    s_id = dao.insert(data)

    assert dao.delete(s_id)
    assert dao.find_by_id(s_id) is None


def test_find_by_name(dao):
    """Test finding suppliers by partial name."""
    dao.insert({"name": "AlphaComp", "contact_info": "a@a.com"})
    dao.insert({"name": "Betta", "contact_info": "b@b.com"})

    results = dao.find_by_name("Alpha")
    assert len(results) == 1
    assert results[0]["name"] == "AlphaComp"
```

### `tests\dao\test_supply_dao.py`

```python
import sqlite3
import pytest
from datetime import date, datetime
from dao.supply_dao import SupplyDAO
from dao.supplier_dao import SupplierDAO
from dao.warehouse_dao import WarehouseDAO
from dao.storekeeper_dao import StorekeeperDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Add related tables and records for FK
    SupplierDAO(conn).insert({"name": "S1", "contact_info": "s1"})
    WarehouseDAO(conn).insert({"name": "W1", "location": "Lviv"})
    StorekeeperDAO(conn).insert({"name": "K1", "warehouse_id": 1})
    return SupplyDAO(conn)


def test_insert_and_find_all(dao):
    """Test inserting and finding all supplies."""
    data = {
        "supply_date": date(2025, 5, 30),
        "supplier_id": 1,
        "warehouse_id": 1,
        "storekeeper_id": 1
    }
    s_id = dao.insert(data)
    assert s_id > 0

    all_s = dao.find_all()
    assert any(x["id"] == s_id for x in all_s)

    # Convert date string back to date object for comparison
    first_supply_date = all_s[0]["supply_date"]
    if isinstance(first_supply_date, str):
        first_supply_date = datetime.fromisoformat(first_supply_date).date()
    assert first_supply_date == date(2025, 5, 30)


def test_find_by_id(dao):
    """Test finding supply by ID."""
    data = {
        "supply_date": date(2024, 1, 1),
        "supplier_id": 1,
        "warehouse_id": 1,
        "storekeeper_id": 1
    }
    s_id = dao.insert(data)

    found = dao.find_by_id(s_id)
    assert found is not None

    # Convert date string to date object for comparison
    found_date = found["supply_date"]
    if isinstance(found_date, str):
        found_date = datetime.fromisoformat(found_date).date()

    assert found_date == date(2024, 1, 1)
    assert found["supplier_id"] == 1
    assert found["warehouse_id"] == 1
    assert found["storekeeper_id"] == 1
```

### `tests\dao\test_supply_record_dao.py`

```python
import sqlite3
import pytest
from datetime import date
from dao.supply_record_dao import SupplyRecordDAO
from dao.supply_dao import SupplyDAO
from dao.component_dao import ComponentDAO
from dao.supplier_dao import SupplierDAO
from dao.warehouse_dao import WarehouseDAO
from dao.storekeeper_dao import StorekeeperDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    # Create all required tables and records for FK
    SupplierDAO(conn).insert({"name": "S1", "contact_info": "s1"})
    WarehouseDAO(conn).insert({"name": "W1", "location": "Lviv"})
    StorekeeperDAO(conn).insert({"name": "K1", "warehouse_id": 1})
    ComponentDAO(conn).insert({"name": "Comp1", "unit": "pcs", "quantity_in_stock": 100})
    SupplyDAO(conn).insert({
        "supply_date": date(2025, 5, 30),
        "supplier_id": 1,
        "warehouse_id": 1,
        "storekeeper_id": 1
    })
    return SupplyRecordDAO(conn)


def test_insert_and_find_by_supply(dao):
    """Test inserting and finding supply records by supply ID."""
    data = {"supply_id": 1, "component_id": 1, "quantity": 42, "price": 3.14}
    rec_id = dao.insert(data)
    assert rec_id > 0

    found = dao.find_by_supply(1)
    assert any(r["id"] == rec_id and r["quantity"] == 42 for r in found)


def test_delete(dao):
    """Test deleting a supply record."""
    data = {"supply_id": 1, "component_id": 1, "quantity": 1, "price": 1.0}
    rec_id = dao.insert(data)

    assert dao.delete(rec_id)
```

### `tests\dao\test_warehouse_dao.py`

```python
import sqlite3
import pytest
from dao.warehouse_dao import WarehouseDAO


@pytest.fixture
def dao():
    conn = sqlite3.connect(':memory:')
    return WarehouseDAO(conn)


def test_insert_and_find_by_id(dao):
    """Test inserting and finding warehouse by ID."""
    data = {"name": "Main", "location": "Kyiv"}
    w_id = dao.insert(data)
    assert w_id > 0

    result = dao.find_by_id(w_id)
    assert result is not None
    assert result["name"] == "Main"
    assert result["location"] == "Kyiv"


def test_update_and_find_all(dao):
    """Test updating warehouse and retrieving all."""
    data = {"name": "Main", "location": "Kyiv"}
    w_id = dao.insert(data)

    # Update
    update_data = {"id": w_id, "name": "Updated", "location": "Kyiv"}
    dao.update(update_data)

    all_ws = dao.find_all()
    assert any(x["name"] == "Updated" for x in all_ws)


def test_delete(dao):
    """Test deleting a warehouse."""
    data = {"name": "Delete", "location": "Lviv"}
    w_id = dao.insert(data)

    ok = dao.delete(w_id)
    assert ok
    assert dao.find_by_id(w_id) is None
```

### `tests\service\__init__.py`

```python

```

### `tests\service\test_component_service.py`

```python
import pytest
from unittest.mock import MagicMock
from services.component_service import ComponentService
from models.component import Component

@pytest.fixture
def dao():
    mock = MagicMock()
    return mock

@pytest.fixture
def service(dao):
    return ComponentService(dao)

def test_increment_stock_valid(service, dao):
    dao.update_quantity.return_value = None
    service.increment_stock(5, 3)
    dao.update_quantity.assert_called_once_with(5, 3)

def test_increment_stock_invalid_id(service):
    with pytest.raises(ValueError):
        service.increment_stock("bad", 2)

def test_increment_stock_invalid_delta(service):
    with pytest.raises(ValueError):
        service.increment_stock(5, "not int")
```

### `tests\service\test_contract_service.py`

```python
from services.contract_service import ContractService
from dao.contract_dao import ContractDAO

class MockContractDAO(ContractDAO):
    def find_by_id(self, contract_id):
        if contract_id == 1:
            class Contract: contact_info = "info"
            return Contract()
        return None

def test_validate_contract_true():
    dao = MockContractDAO()
    service = ContractService(dao)
    assert service.validate_contract(1) is True

def test_validate_contract_false():
    dao = MockContractDAO()
    service = ContractService(dao)
    assert service.validate_contract(9999) is False
```

### `tests\service\test_history_service.py`

```python
from services.history_service import HistoryService
from dao.history_dao import HistoryDAO

class MockHistoryDAO(HistoryDAO):
    def fetch_records(self, filters=None):
        return ["rec1", "rec2"]

def test_get_history_returns_records():
    dao = MockHistoryDAO()
    service = HistoryService(dao)
    result = service.get_history()
    assert result == ["rec1", "rec2"]
```

### `tests\service\test_inventory_observer.py`

```python
from unittest.mock import MagicMock
from services.inventory_observer import InventoryObserver


def test_update_calls_update_quantity():
    """Test that observer calls update_quantity with correct params."""
    dao = MagicMock()
    obs = InventoryObserver(dao)

    # Pass dict instead of model object
    record_data = {"supply_id": 1, "component_id": 2, "quantity": 5, "price": 99.99}
    obs.update(record_data)

    dao.update_quantity.assert_called_once_with(2, 5)
```

### `tests\service\test_receipt_service.py`

```python
from services.receipt_service import ReceiptService

class MockSupplyDAO:
    def find_by_id(self, id):
        return {"id": id}

class MockSupplyRecordDAO:
    def find_by_supply(self, supply_id):
        return [{"rec": 1}]

def test_get_receipt_returns_data():
    supply_dao = MockSupplyDAO()
    record_dao = MockSupplyRecordDAO()
    service = ReceiptService(supply_dao, record_dao)
    receipt = service.get_receipt(5)
    assert receipt["supply"] == {"id": 5}
    assert receipt["records"] == [{"rec": 1}]
```

### `tests\service\test_record_service.py`

```python
from services.record_service import RecordService
from dao.supply_record_dao import SupplyRecordDAO

class MockSupplyRecordDAO(SupplyRecordDAO):
    def __init__(self):
        pass
    def insert(self, record):
        return 123
    def delete(self, record_id):
        return True
    def find_by_supply(self, supply_id):
        return ["recX"]

def test_add_record():
    dao = MockSupplyRecordDAO()
    service = RecordService(dao)
    assert service.add_record({"fake": "record"}) == 123

def test_delete_record():
    dao = MockSupplyRecordDAO()
    service = RecordService(dao)
    assert service.delete_record(7) is True

def test_get_records_by_supply():
    dao = MockSupplyRecordDAO()
    service = RecordService(dao)
    assert service.get_records_by_supply(42) == ["recX"]
```

### `tests\service\test_report_service.py`

```python
import pytest
from unittest.mock import MagicMock
from services.report_service import ReportService


def test_export_unknown_type():
    service = ReportService()
    with pytest.raises(ValueError):
        service.export("txt", [])


def test_export_csv_uses_strategy(monkeypatch):
    service = ReportService()
    mock = MagicMock()
    monkeypatch.setattr("services.report_service.CSVExportStrategy", lambda: mock)
    service.export("csv", [{"x": 1}], "out.csv")
    mock.export.assert_called_once()
```

### `tests\service\test_supplier_service.py`

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from services.supplier_service import SupplierService


class MockSupplierDAO:
    """Mock DAO for testing."""

    def __init__(self):
        self.data = {}
        self.auto_id = 1

    def insert(self, data: dict) -> int:
        """Insert supplier data and return ID."""
        supplier_id = self.auto_id
        self.data[supplier_id] = {**data, "id": supplier_id}
        self.auto_id += 1
        return supplier_id

    def find_all(self) -> list[dict]:
        """Return all suppliers as dicts."""
        return list(self.data.values())


def test_create_supplier():
    """Test creating a supplier through service."""
    dao = MockSupplierDAO()
    service = SupplierService(dao)

    # Pass dict instead of model
    supplier_data = {"name": "ACME", "contact_info": "acme@example.com"}
    supplier_id = service.create(supplier_data)

    assert supplier_id == 1
    assert len(service.list_all()) == 1
    assert service.list_all()[0].name == "ACME"
```

### `tests\service\test_supply_service.py`

```python
import pytest
from unittest.mock import MagicMock
from services.supply_service import SupplyService
from models.supply import Supply
from models.supply_record import SupplyRecord
from datetime import date


@pytest.fixture
def supply_dao():
    return MagicMock()


@pytest.fixture
def record_dao():
    return MagicMock()


@pytest.fixture
def service(supply_dao, record_dao):
    return SupplyService(supply_dao, record_dao)


def test_register_supply_ok(service, supply_dao, record_dao):
    """Test successful supply registration."""
    supply = Supply(
        supply_date=date(2024, 5, 30),
        supplier_id=1,
        warehouse_id=1,
        storekeeper_id=1
    )
    records = [
        SupplyRecord(supply_id=None, component_id=1, quantity=10, price=100.0),
        SupplyRecord(supply_id=None, component_id=2, quantity=5, price=50.0)
    ]

    # Mock DAO to return ID
    supply_dao.insert.return_value = 1
    record_dao.insert.side_effect = [1, 2]  # Return IDs for records

    result = service.register({"supply": supply, "records": records})

    # Verify DAO was called with dict (not model object)
    assert supply_dao.insert.called
    call_args = supply_dao.insert.call_args[0][0]
    assert isinstance(call_args, dict)
    assert call_args["supplier_id"] == 1

    # Verify all records got supply_id set
    assert all(r.supply_id == 1 for r in records)
    assert record_dao.insert.call_count == 2
    assert result == "<<SupplySaved>>"


def test_register_supply_empty_records(service):
    """Test that empty records raises ValueError."""
    supply = Supply(
        supply_date=date(2024, 5, 30),
        supplier_id=1,
        warehouse_id=1,
        storekeeper_id=1
    )
    with pytest.raises(ValueError):
        service.register({"supply": supply, "records": []})
```

### `tests\test_gui_stub.py`

```python
# Тест чорного ящика через tkinter не виконується тут,
# але драйвер показує, що вікно SupplyWindow створюється без помилок.
import sys
import os
import pytest
if not os.environ.get("DISPLAY") and os.name != "nt":
    pytest.skip("No display – GUI tests skipped", allow_module_level=True)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import TclError
from ui.supply_window import SupplyWindow

def test_supply_window_creation(monkeypatch):
    try:
        root = tk.Tk()
    except TclError:
        pytest.skip("Tk not available")
    # Перехоплюємо метод center_window, щоб не відкривалось GUI.
    monkeypatch.setattr(SupplyWindow, 'center_window', lambda self, w, h: None)
    win = tk.Toplevel(root)
    SupplyWindow(win)
    assert win.winfo_exists() == 1
    win.destroy()
    root.destroy()
```

### `tests\test_usecase_mapping.py`

```python
import pytest
from controllers.report_controller import ReportController
from controllers.supplier_controller import SupplierController
from controllers.component_controller import ComponentController
from controllers.supply_controller import SupplyController
from controllers.orders_controller import OrderController, OrdersController

def test_report_controller_methods():
    assert hasattr(ReportController, "generate_report")
    assert hasattr(ReportController, "show_supply_history")


def test_supplier_controller_methods():
    assert hasattr(SupplierController, "on_add")
    assert hasattr(SupplierController, "on_update")
    assert hasattr(SupplierController, "on_delete")


def test_component_controller_methods():
    assert hasattr(ComponentController, "on_add")
    assert hasattr(ComponentController, "on_update")
    assert hasattr(ComponentController, "on_delete")


def test_supply_controller_methods():
    assert hasattr(SupplyController, "register_supply")


def test_order_controller_methods():
    assert hasattr(OrdersController, "create_order")
    assert hasattr(OrdersController, "check_contract")
```

---

## Статистика

**Всього файлів**: 131

### Файлів по категоріях:

- **Documentation**: 8
- **Root**: 3
- **Backend - Config**: 7
- **Backend - Core**: 4
- **Backend - Database**: 4
- **Backend - Models**: 8
- **Backend - DAO**: 11
- **Backend - Services**: 13
- **Backend - API**: 7
- **Frontend - Config**: 9
- **Frontend - Services**: 6
- **Frontend - Hooks**: 1
- **Frontend - Pages**: 7
- **Frontend - Components**: 22
- **Tests**: 21
