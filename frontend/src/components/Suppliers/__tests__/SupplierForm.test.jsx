/**
 * Тести на основі таблиці рішень для SupplierForm
 *
 * Таблиця рішень #8: Валідація форми постачальника
 *
 * Правила:
 * - R1: Всі поля валідні - успішне збереження
 * - R2: Порожня назва - alert помилки
 * - R3: Порожній контакт - успіх (опціонально)
 * - R4: Форма працює з onSubmit callback
 * - R5: Оновлення існуючого постачальника
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import SupplierForm from '../SupplierForm';

// Mock window.alert
global.alert = vi.fn();

describe('SupplierForm - Decision Table Tests', () => {
  const mockOnSubmit = vi.fn();
  const mockOnCancel = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('R1: Всі поля валідні - успішне збереження', () => {
    it('повинен успішно викликати onSubmit з валідними даними', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<SupplierForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act
      const nameInput = screen.getByPlaceholderText(/Введіть назву постачальника/i);
      const contactInput = screen.getByPlaceholderText(/Телефон, email, адреса/i);

      await user.type(nameInput, 'Test Supplier');
      await user.type(contactInput, 'test@example.com');

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      expect(mockOnSubmit).toHaveBeenCalledWith({
        name: 'Test Supplier',
        contact_info: 'test@example.com',
      });
    });
  });

  describe('R2: Порожня назва - помилка валідації', () => {
    it('повинен запобігти відправці форми з порожньою назвою', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<SupplierForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act - вводимо тільки контакт, назву залишаємо порожньою
      const contactInput = screen.getByPlaceholderText(/Телефон, email, адреса/i);
      await user.type(contactInput, 'test@example.com');

      const nameInput = screen.getByPlaceholderText(/Введіть назву постачальника/i);
      await user.type(nameInput, '   '); // Тільки пробіли
      await user.clear(nameInput);

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert - форма не повинна відправлятися через валідацію
      // (HTML5 required або JavaScript trim перевірка)
      expect(mockOnSubmit).not.toHaveBeenCalled();
    });
  });

  describe('R3: Порожній контакт - успіх', () => {
    it('повинен успішно викликати onSubmit без контакту', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<SupplierForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act
      const nameInput = screen.getByPlaceholderText(/Введіть назву постачальника/i);
      await user.type(nameInput, 'Supplier No Contact');

      const submitButton = screen.getByRole('button', { name: /Створити/i });
      await user.click(submitButton);

      // Assert
      expect(mockOnSubmit).toHaveBeenCalledWith({
        name: 'Supplier No Contact',
        contact_info: '',
      });
    });
  });

  describe('R4: Кнопка скасування', () => {
    it('повинен викликати onCancel при натисканні Скасувати', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<SupplierForm onSubmit={mockOnSubmit} onCancel={mockOnCancel} />);

      // Act
      const cancelButton = screen.getByRole('button', { name: /Скасувати/i });
      await user.click(cancelButton);

      // Assert
      expect(mockOnCancel).toHaveBeenCalled();
      expect(mockOnSubmit).not.toHaveBeenCalled();
    });
  });

  describe('R5: Оновлення існуючого постачальника', () => {
    it('повинен показати Зберегти для існуючого постачальника', async () => {
      // Arrange
      const user = userEvent.setup();
      const existingSupplier = {
        id: 1,
        name: 'Existing Supplier',
        contact_info: 'old@example.com',
      };

      render(
        <SupplierForm
          supplier={existingSupplier}
          onSubmit={mockOnSubmit}
          onCancel={mockOnCancel}
        />
      );

      // Assert - перевіряємо що форма заповнена даними
      expect(screen.getByDisplayValue('Existing Supplier')).toBeInTheDocument();
      expect(screen.getByDisplayValue('old@example.com')).toBeInTheDocument();
      expect(screen.getByRole('button', { name: /Зберегти/i })).toBeInTheDocument();

      // Act - оновлюємо назву
      const nameInput = screen.getByDisplayValue('Existing Supplier');
      await user.clear(nameInput);
      await user.type(nameInput, 'Updated Supplier');

      const submitButton = screen.getByRole('button', { name: /Зберегти/i });
      await user.click(submitButton);

      // Assert
      expect(mockOnSubmit).toHaveBeenCalledWith({
        name: 'Updated Supplier',
        contact_info: 'old@example.com',
      });
    });
  });
});
