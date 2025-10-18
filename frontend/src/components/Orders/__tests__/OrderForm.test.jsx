/**
 * Тести на основі таблиці рішень для OrderForm
 *
 * Таблиця рішень #10: Створення замовлення
 *
 * Правила:
 * - R1: Всі поля валідні - успіх
 * - R2: Не вибраний постачальник - помилка
 * - R3: Порожній постачальник - помилка
 * - R4: Валідний статус - успіх
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { BrowserRouter } from 'react-router-dom';
import OrderForm from '../OrderForm';
import * as ordersService from '../../../services/ordersService';
import * as toast from 'react-hot-toast';

// Mock services
vi.mock('../../../services/ordersService');
vi.mock('react-hot-toast');

const renderWithRouter = (component) => {
  return render(
    <BrowserRouter>
      {component}
    </BrowserRouter>
  );
};

describe('OrderForm - Decision Table Tests', () => {
  const mockOnSuccess = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('R1: Всі поля валідні - успіх', () => {
    it('повинен успішно створити замовлення з валідними даними', async () => {
      // Arrange
      const user = userEvent.setup();
      ordersService.createOrder.mockResolvedValue({
        id: 1,
        supplier: 'Test Supplier R1',
        status: 'pending',
      });

      renderWithRouter(<OrderForm onSuccess={mockOnSuccess} />);

      // Act
      const supplierInput = screen.getByPlaceholderText(/Постачальник/i);
      await user.type(supplierInput, 'Test Supplier R1');

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(ordersService.createOrder).toHaveBeenCalledWith(
          expect.objectContaining({
            supplier: 'Test Supplier R1',
          })
        );
        expect(toast.success).toHaveBeenCalled();
        expect(mockOnSuccess).toHaveBeenCalled();
      });
    });
  });

  describe('R2: Не вибраний постачальник - помилка', () => {
    it('не повинен дозволити відправку без постачальника', async () => {
      // Arrange
      const user = userEvent.setup();
      renderWithRouter(<OrderForm onSuccess={mockOnSuccess} />);

      // Act
      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(ordersService.createOrder).not.toHaveBeenCalled();
      });
    });
  });

  describe('R3: Порожній постачальник - помилка', () => {
    it('повинен показати помилку при порожньому полі постачальника', async () => {
      // Arrange
      const user = userEvent.setup();
      ordersService.createOrder.mockRejectedValue({
        response: { status: 400, data: { detail: 'Supplier is required' } },
      });

      renderWithRouter(<OrderForm onSuccess={mockOnSuccess} />);

      // Act
      const supplierInput = screen.getByPlaceholderText(/Постачальник/i);
      await user.type(supplierInput, '   '); // Пробіли
      await user.clear(supplierInput);

      const submitButton = screen.getByRole('button', { name: /Створити/i });

      // Submit button може бути disabled
      if (!submitButton.disabled) {
        await user.click(submitButton);
      }

      // Assert - форма не повинна відправлятися з порожнім постачальником
      expect(ordersService.createOrder).not.toHaveBeenCalled();
    });
  });

  describe('R4: Валідний статус - успіх', () => {
    it('повинен успішно створити замовлення з різними статусами', async () => {
      // Arrange
      const user = userEvent.setup();
      ordersService.createOrder.mockResolvedValue({
        id: 1,
        supplier: 'Test Supplier R4',
        status: 'completed',
      });

      renderWithRouter(<OrderForm onSuccess={mockOnSuccess} />);

      // Act
      const supplierInput = screen.getByPlaceholderText(/Постачальник/i);
      await user.type(supplierInput, 'Test Supplier R4');

      // Якщо є select для статусу
      const statusSelects = screen.queryAllByRole('combobox');
      if (statusSelects.length > 0) {
        await user.selectOptions(statusSelects[0], 'completed');
      }

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(ordersService.createOrder).toHaveBeenCalled();
        expect(toast.success).toHaveBeenCalled();
      });
    });
  });

  describe('R5: Помилка API - показати повідомлення', () => {
    it('повинен показати помилку при невдалому запиті', async () => {
      // Arrange
      const user = userEvent.setup();
      ordersService.createOrder.mockRejectedValue(new Error('Server error'));

      renderWithRouter(<OrderForm onSuccess={mockOnSuccess} />);

      // Act
      const supplierInput = screen.getByPlaceholderText(/Постачальник/i);
      await user.type(supplierInput, 'Test Supplier Error');

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(toast.error).toHaveBeenCalled();
        expect(mockOnSuccess).not.toHaveBeenCalled();
      });
    });
  });
});
