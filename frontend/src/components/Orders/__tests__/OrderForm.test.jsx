/**
 * Тести на основі таблиці рішень для OrderForm
 *
 * Таблиця рішень #10: Створення замовлення
 *
 * Правила:
 * - R1: Всі поля валідні - успіх
 * - R2: Порожній постачальник - alert помилки
 * - R3: Зміна статусу замовлення
 * - R4: Кнопка скасування
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import OrderForm from '../OrderForm';

// Mock window.alert
global.alert = vi.fn();

describe('OrderForm - Decision Table Tests', () => {
  const mockOnSubmit = vi.fn();
  const mockOnCancel = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('R1: Всі поля валідні - успіх', () => {
    it('повинен успішно викликати onSubmit з валідними даними', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<OrderForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act
      const supplierInput = screen.getByPlaceholderText(/Введіть назву постачальника/i);
      await user.type(supplierInput, 'Test Supplier');

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      expect(mockOnSubmit).toHaveBeenCalledWith({
        supplier: 'Test Supplier',
        status: 'pending', // Статус за замовчуванням
      });
    });
  });

  describe('R2: Порожній постачальник - помилка валідації', () => {
    it('повинен запобігти відправці з порожнім постачальником', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<OrderForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act - вводимо пробіли і очищаємо
      const supplierInput = screen.getByPlaceholderText(/Введіть назву постачальника/i);
      await user.type(supplierInput, '   ');
      await user.clear(supplierInput);

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert - форма не повинна відправлятися через валідацію
      expect(mockOnSubmit).not.toHaveBeenCalled();
    });
  });

  describe('R3: Зміна статусу замовлення', () => {
    it('повинен дозволити вибрати різні статуси', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<OrderForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act
      const supplierInput = screen.getByPlaceholderText(/Введіть назву постачальника/i);
      await user.type(supplierInput, 'Test Supplier');

      const statusSelect = screen.getByRole('combobox');
      await user.selectOptions(statusSelect, 'confirmed');

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      expect(mockOnSubmit).toHaveBeenCalledWith({
        supplier: 'Test Supplier',
        status: 'confirmed',
      });
    });

    it('повинен підтримувати всі статуси замовлення', async () => {
      // Arrange
      render(<OrderForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Assert
      const statusSelect = screen.getByRole('combobox');
      expect(statusSelect).toHaveTextContent('Очікує');
      expect(statusSelect).toHaveTextContent('Підтверджено');
      expect(statusSelect).toHaveTextContent('Доставлено');
      expect(statusSelect).toHaveTextContent('Скасовано');
    });
  });

  describe('R4: Кнопка скасування', () => {
    it('повинен викликати onCancel при натисканні Скасувати', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<OrderForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act
      const cancelButton = screen.getByRole('button', { name: /Скасувати/i });
      await user.click(cancelButton);

      // Assert
      expect(mockOnCancel).toHaveBeenCalled();
      expect(mockOnSubmit).not.toHaveBeenCalled();
    });
  });
});
