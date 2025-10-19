# Frontend Testing Guide

## Налаштування тестування

Проект використовує **Vitest** + **React Testing Library** для тестування.

### Встановлені залежності:

```json
{
  "@testing-library/react": "^14.1.2",
  "@testing-library/jest-dom": "^6.1.5",
  "@testing-library/user-event": "^14.5.1",
  "@vitest/ui": "^1.1.0",
  "@vitest/coverage-v8": "^1.1.0",
  "jsdom": "^23.0.1",
  "vitest": "^1.1.0"
}
```

## Структура тестів

```
src/
├── components/
│   ├── Suppliers/
│   │   └── __tests__/
│   │       └── SupplierForm.test.jsx
│   ├── Components/
│   │   └── __tests__/
│   │       └── ComponentsList.test.jsx
│   └── Orders/
│       └── __tests__/
│           └── OrderForm.test.jsx
└── setupTests.js
```

## Запуск тестів

### Встановлення залежностей

```bash
cd frontend
npm install
```

### Команди тестування

```bash
# Запустити всі тести
npm test

# Запустити тести у watch режимі
npm test -- --watch

# Запустити тести з покриттям коду
npm test:coverage

# Запустити тести з UI (візуальний інтерфейс)
npm test:ui

# Запустити конкретний файл тестів
npm test -- SupplierForm.test.jsx

# Запустити тести що містять "decision" в назві
npm test -- decision
```

## Написані тести

### 1. SupplierForm.test.jsx (5 тестів)

**Таблиця рішень #8: Валідація форми постачальника**

- ✅ R1: Всі поля валідні - успішне збереження
- ✅ R2: Порожня назва - помилка
- ✅ R3: Порожній контакт - успіх
- ✅ R4: Помилка API - показати повідомлення
- ✅ R5: Оновлення існуючого постачальника

```bash
npm test -- SupplierForm
```

### 2. ComponentsList.test.jsx (5 тестів)

**Таблиця рішень #9: Видалення компонента**

- ✅ R1: Успішне видалення
- ✅ R2: API помилка
- ✅ R3: Неіснуючий компонент (404)
- ✅ R4: Завантаження списку
- ✅ R5: Порожній список

```bash
npm test -- ComponentsList
```

### 3. OrderForm.test.jsx (5 тестів)

**Таблиця рішень #10: Створення замовлення**

- ✅ R1: Всі поля валідні - успіх
- ✅ R2: Не вибраний постачальник - помилка
- ✅ R3: Порожній постачальник - помилка
- ✅ R4: Валідний статус - успіх
- ✅ R5: Помилка API

```bash
npm test -- OrderForm
```

## Приклад виконання тестів

```bash
$ npm test

 ✓ src/components/Suppliers/__tests__/SupplierForm.test.jsx (5)
   ✓ R1: Всі поля валідні - успішне збереження
   ✓ R2: Порожня назва - помилка
   ✓ R3: Порожній контакт - успіх
   ✓ R4: Помилка API - показати повідомлення
   ✓ R5: Оновлення існуючого постачальника

 ✓ src/components/Components/__tests__/ComponentsList.test.jsx (5)
   ✓ R1: Успішне видалення
   ✓ R2: API помилка
   ✓ R3: Неіснуючий компонент
   ✓ R4: Завантаження списку
   ✓ R5: Порожній список

 ✓ src/components/Orders/__tests__/OrderForm.test.jsx (5)
   ✓ R1: Всі поля валідні - успіх
   ✓ R2: Не вибраний постачальник - помилка
   ✓ R3: Порожній постачальник - помилка
   ✓ R4: Валідний статус - успіх
   ✓ R5: Помилка API

Test Files  3 passed (3)
     Tests  15 passed (15)
```

## Покриття коду

Переглянути звіт покриття:

```bash
npm test:coverage
```

Звіт буде згенеровано в `coverage/index.html`

## Додавання нових тестів

### Приклад тесту:

```javascript
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import MyComponent from '../MyComponent';

describe('MyComponent', () => {
  it('should render correctly', () => {
    render(<MyComponent />);
    expect(screen.getByText('Hello')).toBeInTheDocument();
  });

  it('should handle click', async () => {
    const user = userEvent.setup();
    const mockFn = vi.fn();

    render(<MyComponent onClick={mockFn} />);

    await user.click(screen.getByRole('button'));

    expect(mockFn).toHaveBeenCalled();
  });
});
```

## Mocking

### Mock API service:

```javascript
vi.mock('../../../services/suppliersService', () => ({
  getAllSuppliers: vi.fn(),
  createSupplier: vi.fn(),
  updateSupplier: vi.fn(),
  deleteSupplier: vi.fn(),
}));
```

### Mock react-hot-toast:

```javascript
vi.mock('react-hot-toast', () => ({
  success: vi.fn(),
  error: vi.fn(),
}));
```

## Best Practices

1. **Використовуйте user-event замість fireEvent** для більш реалістичних взаємодій
2. **Очікуйте за допомогою waitFor** для асинхронних операцій
3. **Тестуйте поведінку, а не реалізацію**
4. **Використовуйте доступні ролі (getByRole)** замість селекторів
5. **Очищайте моки перед кожним тестом** (beforeEach)

## Troubleshooting

### Помилка: "Cannot find module"

```bash
npm install
```

### Помилка: "ReferenceError: navigator is not defined"

Переконайтеся, що `vitest.config.js` налаштовано з `environment: 'jsdom'`

### Тести падають через CSS

CSS ігнорується за замовчуванням у конфігурації Vitest.

## Корисні посилання

- [Vitest Documentation](https://vitest.dev/)
- [React Testing Library](https://testing-library.com/react)
- [Testing Library Queries](https://testing-library.com/docs/queries/about)
- [User Event](https://testing-library.com/docs/user-event/intro)
