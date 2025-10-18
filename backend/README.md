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
