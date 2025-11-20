# Функціональні діаграми - Лабораторна робота №4

## Швидкий доступ

### 📚 Документація
- **[FUNCTIONAL_DIAGRAMS_GUIDE.md](FUNCTIONAL_DIAGRAMS_GUIDE.md)** - Повний гайд з теорії та практики
  - Теоретичні основи (булевські оператори, обмеження)
  - Покрокова інструкція побудови діаграм
  - 5 детальних прикладів для проекту з кодом тестів

- **[FUNCTIONAL_DIAGRAMS_TEST_RESULTS.md](FUNCTIONAL_DIAGRAMS_TEST_RESULTS.md)** - Результати тестування
  - Підсумкові результати (15 passed, 6 skipped, 4 failed)
  - Детальний аналіз по кожній діаграмі
  - Виявлені проблеми API та рекомендації

### 🧪 Тестові файли
- `backend/tests/api/test_suppliers_functional_diagram.py` - Тести для постачальників
- `backend/tests/api/test_components_functional_diagram.py` - Тести для компонентів
- `backend/tests/api/test_orders_functional_diagram.py` - Тести для замовлень

---

## Швидкий старт

### Запуск тестів

```bash
cd backend

# Всі функціональні діаграми
python -m pytest tests/api/test_*_functional_diagram.py -v

# Тільки suppliers
python -m pytest tests/api/test_suppliers_functional_diagram.py -v

# З покриттям коду
python -m pytest tests/api/test_*_functional_diagram.py --cov=app --cov-report=html
```

### Результати

```
✅ PASSED: 15 tests (60%)
⚠️  SKIPPED: 6 tests (24%)
❌ FAILED: 4 tests (16%)

Загалом: 5 діаграм, 25 тестів, ~0.5s
```

---

## Структура діаграм

### 1. Створення постачальника (Suppliers)
- **Причини:** name надано, name унікальне
- **Наслідки:** Success 201, Error 422, Error 400
- **Проблеми:** ❌ Відсутня валідація унікальності

### 2. Створення компонента (Components)
- **Причини:** name, unit, qty >= 0
- **Наслідки:** Success 201, Error 422 (для кожного поля)
- **Проблеми:** ❌ Немає валідації qty >= 0

### 3. Створення замовлення (Orders)
- **Причини:** supplier, status (pending/completed/cancelled)
- **Наслідки:** Success 201, Error 422, Error 400
- **Проблеми:** ❌ Немає enum валідації для status

### 4. Оновлення компонента
- **Причини:** id існує, name, unit, qty >= 0
- **Наслідки:** Success 200, Error 404, Error 422
- **Проблеми:** ❌ Немає валідації qty >= 0

### 5. Видалення постачальника
- **Причини:** id існує, немає замовлень
- **Наслідки:** Success 200, Error 404, Error 400
- **Проблеми:** ⚠️ Немає перевірки залежностей

---

## Виявлені проблеми API

| #  | Проблема | Пріоритет | Тест |
|----|----------|-----------|------|
| 1  | Відсутня валідація унікальності name у suppliers | 🔴 Високий | test_T3_duplicate_name |
| 2  | Немає валідації qty >= 0 у components | 🔴 Високий | test_T4_negative_qty |
| 3  | Немає enum валідації status у orders | 🔴 Високий | test_T5_invalid_status |
| 4  | Немає перевірки залежностей при видаленні | ⚠️ Середній | test_T3_delete_with_orders |
| 5  | Неправильні HTTP коди помилок | ⚠️ Середній | test_T2_empty_name |

---

## Рекомендації для виправлення

### 1. Валідація унікальності (Suppliers)

```python
# У SupplierService.create()
existing = self.dao.get_by_name(name)
if existing:
    raise ValueError("Supplier with this name already exists")
```

### 2. Валідація негативних значень (Components)

```python
from pydantic import Field

class ComponentCreate(BaseModel):
    qty: int = Field(default=0, ge=0)  # ge = greater or equal
```

### 3. Enum для статусу (Orders)

```python
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class OrderCreate(BaseModel):
    status: OrderStatus = OrderStatus.PENDING
```

### 4. Перевірка залежностей (Suppliers)

```python
# У SupplierService.delete()
orders = self.order_dao.get_by_supplier_id(supplier_id)
if orders:
    raise ValueError("Cannot delete supplier with active orders")
```

---

## Переваги методу

✅ **Систематичність** - Покриття всіх комбінацій входів
✅ **Документування** - Візуалізація логіки системи
✅ **Автоматизація** - Легко генерувати тести
✅ **Виявлення помилок** - Знайдено 5 критичних проблем

---

## Автор

**Бецьков Б.І., група АС-232**
**Лабораторна робота №4** - Тестування за допомогою функціональних діаграм
**2025 рік**
