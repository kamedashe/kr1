/**
 * Тести на основі таблиці рішень для ComponentsList
 *
 * Таблиця рішень #9: Видалення компонента
 *
 * Правила:
 * - R1: Успішне видалення з підтвердженням
 * - R2: Скасування видалення
 * - R3: API помилка при видаленні
 * - R4: Завантаження та відображення списку
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import ComponentsList from '../ComponentsList';
import { componentsService } from '../../../services/componentsService';

// Mock services
vi.mock('../../../services/componentsService');

// Mock window.confirm and alert
global.confirm = vi.fn();
global.alert = vi.fn();

describe('ComponentsList - Decision Table: Видалення', () => {
  const mockComponents = [
    { id: 1, name: 'Component 1', unit: 'шт', qty: 10 },
    { id: 2, name: 'Component 2', unit: 'кг', qty: 20 },
  ];

  beforeEach(() => {
    vi.clearAllMocks();
    // За замовчуванням завантаження успішне
    componentsService.getAll.mockResolvedValue(mockComponents);
  });

  describe('R1: Успішне видалення з підтвердженням', () => {
    it('повинен видалити компонент після підтвердження', async () => {
      // Arrange
      const user = userEvent.setup();
      global.confirm.mockReturnValue(true); // Підтверджуємо видалення
      componentsService.delete.mockResolvedValue();

      render(<ComponentsList />);

      // Чекаємо завантаження компонентів
      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
      });

      // Act
      const deleteButtons = screen.getAllByRole('button', { name: /Видалити/i });
      await user.click(deleteButtons[0]);

      // Assert
      expect(global.confirm).toHaveBeenCalledWith('Ви впевнені, що хочете видалити це комплектуюче?');
      await waitFor(() => {
        expect(componentsService.delete).toHaveBeenCalledWith(1);
      });
    });
  });

  describe('R2: Скасування видалення', () => {
    it('не повинен видаляти компонент при скасуванні', async () => {
      // Arrange
      const user = userEvent.setup();
      global.confirm.mockReturnValue(false); // Скасовуємо видалення

      render(<ComponentsList />);

      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
      });

      // Act
      const deleteButtons = screen.getAllByRole('button', { name: /Видалити/i });
      await user.click(deleteButtons[0]);

      // Assert
      expect(global.confirm).toHaveBeenCalled();
      expect(componentsService.delete).not.toHaveBeenCalled();
    });
  });

  describe('R3: API помилка при видаленні', () => {
    it('повинен показати alert при помилці видалення', async () => {
      // Arrange
      const user = userEvent.setup();
      global.confirm.mockReturnValue(true);
      componentsService.delete.mockRejectedValue(new Error('Network error'));

      render(<ComponentsList />);

      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
      });

      // Act
      const deleteButtons = screen.getAllByRole('button', { name: /Видалити/i });
      await user.click(deleteButtons[0]);

      // Assert
      await waitFor(() => {
        expect(global.alert).toHaveBeenCalledWith('Не вдалося видалити комплектуюче');
      });
    });
  });

  describe('R4: Завантаження та відображення списку', () => {
    it('повинен показати список компонентів при завантаженні', async () => {
      // Act
      render(<ComponentsList />);

      // Assert
      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
        expect(screen.getByText('Component 2')).toBeInTheDocument();
      });
    });

    it('повинен показати повідомлення "Завантаження..." під час завантаження', () => {
      // Arrange - затримуємо відповідь
      componentsService.getAll.mockImplementation(() => new Promise(() => {}));

      // Act
      render(<ComponentsList />);

      // Assert
      expect(screen.getByText('Завантаження...')).toBeInTheDocument();
    });

    it('повинен показати помилку при невдалому завантаженні', async () => {
      // Arrange
      componentsService.getAll.mockRejectedValue(new Error('Network error'));

      // Act
      render(<ComponentsList />);

      // Assert
      await waitFor(() => {
        expect(screen.getByText('Не вдалося завантажити комплектуючі')).toBeInTheDocument();
      });
    });
  });
});
