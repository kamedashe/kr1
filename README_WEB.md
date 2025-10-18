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
