/**
 * Тести на основі таблиці рішень для SupplierForm
 *
 * Таблиця рішень #8: Валідація форми постачальника
 *
 * Правила:
 * - R1: Всі поля валідні - успішне збереження
 * - R2: Порожня назва - помилка
 * - R3: Порожній контакт - успіх (опціонально)
 * - R4: Невалідний email - помилка
 * - R5: Форма не відправлена - кнопка заблокована
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { BrowserRouter } from 'react-router-dom';
import SupplierForm from '../SupplierForm';
import * as suppliersService from '../../../services/suppliersService';
import * as toast from 'react-hot-toast';

// Mock services
vi.mock('../../../services/suppliersService');
vi.mock('react-hot-toast');

const renderWithRouter = (component) => {
  return render(
    <BrowserRouter>
      {component}
    </BrowserRouter>
  );
};

describe('SupplierForm - Decision Table Tests', () => {
  const mockOnSuccess = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('R1: Всі поля валідні - успішне збереження', () => {
    it('повинен успішно створити постачальника з валідними даними', async () => {
      // Arrange
      const user = userEvent.setup();
      suppliersService.createSupplier.mockResolvedValue({
        id: 1,
        name: 'Test Supplier',
        contact_info: 'test@example.com',
      });

      renderWithRouter(<SupplierForm onSuccess={mockOnSuccess} />);

      // Act
      const nameInput = screen.getByPlaceholderText(/Назва постачальника/i);
      const contactInput = screen.getByPlaceholderText(/Контактна інформація/i);

      await user.type(nameInput, 'Test Supplier');
      await user.type(contactInput, 'test@example.com');

      const submitButton = screen.getByRole('button', { name: /Зберегти/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(suppliersService.createSupplier).toHaveBeenCalledWith({
          name: 'Test Supplier',
          contact_info: 'test@example.com',
        });
        expect(toast.success).toHaveBeenCalled();
        expect(mockOnSuccess).toHaveBeenCalled();
      });
    });
  });

  describe('R2: Порожня назва - помилка', () => {
    it('повинен показати помилку при порожній назві', async () => {
      // Arrange
      const user = userEvent.setup();
      renderWithRouter(<SupplierForm onSuccess={mockOnSuccess} />);

      // Act
      const contactInput = screen.getByPlaceholderText(/Контактна інформація/i);
      await user.type(contactInput, 'test@example.com');

      const submitButton = screen.getByRole('button', { name: /Зберегти/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(suppliersService.createSupplier).not.toHaveBeenCalled();
        // Форма не повинна відправлятися без назви
      });
    });
  });

  describe('R3: Порожній контакт - успіх', () => {
    it('повинен успішно створити постачальника без контакту', async () => {
      // Arrange
      const user = userEvent.setup();
      suppliersService.createSupplier.mockResolvedValue({
        id: 1,
        name: 'Supplier No Contact',
      });

      renderWithRouter(<SupplierForm onSuccess={mockOnSuccess} />);

      // Act
      const nameInput = screen.getByPlaceholderText(/Назва постачальника/i);
      await user.type(nameInput, 'Supplier No Contact');

      const submitButton = screen.getByRole('button', { name: /Зберегти/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(suppliersService.createSupplier).toHaveBeenCalledWith({
          name: 'Supplier No Contact',
          contact_info: '',
        });
        expect(toast.success).toHaveBeenCalled();
      });
    });
  });

  describe('R4: Помилка API - показати повідомлення', () => {
    it('повинен показати помилку при невдалому запиті', async () => {
      // Arrange
      const user = userEvent.setup();
      const errorMessage = 'Network error';
      suppliersService.createSupplier.mockRejectedValue(new Error(errorMessage));

      renderWithRouter(<SupplierForm onSuccess={mockOnSuccess} />);

      // Act
      const nameInput = screen.getByPlaceholderText(/Назва постачальника/i);
      await user.type(nameInput, 'Test Supplier');

      const submitButton = screen.getByRole('button', { name: /Зберегти/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(toast.error).toHaveBeenCalled();
        expect(mockOnSuccess).not.toHaveBeenCalled();
      });
    });
  });

  describe('R5: Оновлення існуючого постачальника', () => {
    it('повинен викликати updateSupplier для існуючого постачальника', async () => {
      // Arrange
      const user = userEvent.setup();
      const existingSupplier = {
        id: 1,
        name: 'Existing Supplier',
        contact_info: 'old@example.com',
      };

      suppliersService.updateSupplier.mockResolvedValue({
        ...existingSupplier,
        name: 'Updated Supplier',
      });

      renderWithRouter(
        <SupplierForm
          supplier={existingSupplier}
          onSuccess={mockOnSuccess}
        />
      );

      // Act
      const nameInput = screen.getByDisplayValue('Existing Supplier');
      await user.clear(nameInput);
      await user.type(nameInput, 'Updated Supplier');

      const submitButton = screen.getByRole('button', { name: /Зберегти/i });
      await user.click(submitButton);

      // Assert
      await waitFor(() => {
        expect(suppliersService.updateSupplier).toHaveBeenCalledWith(1, {
          name: 'Updated Supplier',
          contact_info: 'old@example.com',
        });
        expect(toast.success).toHaveBeenCalled();
      });
    });
  });
});
