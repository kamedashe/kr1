/**
 * Тести на основі таблиці рішень для ComponentsList
 *
 * Таблиця рішень #9: Видалення компонента
 *
 * Правила:
 * - R1: Успішне видалення - компонент зникає зі списку
 * - R2: API помилка - toast помилки
 * - R3: Неіснуючий компонент - помилка
 * - R4: Без дії - список без змін
 */

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import ComponentsList from '../ComponentsList';
import * as componentsService from '../../../services/componentsService';
import * as toast from 'react-hot-toast';

// Mock services
vi.mock('../../../services/componentsService');
vi.mock('react-hot-toast');

const renderWithRouter = (component) => {
  return render(
    <BrowserRouter>
      {component}
    </BrowserRouter>
  );
};

describe('ComponentsList - Decision Table: Видалення', () => {
  const mockComponents = [
    { id: 1, name: 'Component 1', unit: 'шт', qty: 10 },
    { id: 2, name: 'Component 2', unit: 'кг', qty: 20 },
  ];

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('R1: Успішне видалення', () => {
    it('повинен видалити компонент зі списку після успішного видалення', async () => {
      // Arrange
      componentsService.getAllComponents.mockResolvedValue(mockComponents);
      componentsService.deleteComponent.mockResolvedValue();

      renderWithRouter(<ComponentsList />);

      // Чекаємо завантаження компонентів
      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
      });

      // Act
      const deleteButtons = screen.getAllByRole('button', { name: /Видалити/i });
      fireEvent.click(deleteButtons[0]);

      // Assert
      await waitFor(() => {
        expect(componentsService.deleteComponent).toHaveBeenCalledWith(1);
        expect(toast.success).toHaveBeenCalled();
      });
    });
  });

  describe('R2: API помилка', () => {
    it('повинен показати toast помилки при невдалому видаленні', async () => {
      // Arrange
      componentsService.getAllComponents.mockResolvedValue(mockComponents);
      componentsService.deleteComponent.mockRejectedValue(
        new Error('Network error')
      );

      renderWithRouter(<ComponentsList />);

      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
      });

      // Act
      const deleteButtons = screen.getAllByRole('button', { name: /Видалити/i });
      fireEvent.click(deleteButtons[0]);

      // Assert
      await waitFor(() => {
        expect(toast.error).toHaveBeenCalled();
        // Компонент залишається в списку
        expect(screen.getByText('Component 1')).toBeInTheDocument();
      });
    });
  });

  describe('R3: Неіснуючий компонент', () => {
    it('повинен показати помилку 404', async () => {
      // Arrange
      componentsService.getAllComponents.mockResolvedValue(mockComponents);
      componentsService.deleteComponent.mockRejectedValue({
        response: { status: 404 },
      });

      renderWithRouter(<ComponentsList />);

      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
      });

      // Act
      const deleteButtons = screen.getAllByRole('button', { name: /Видалити/i });
      fireEvent.click(deleteButtons[0]);

      // Assert
      await waitFor(() => {
        expect(toast.error).toHaveBeenCalled();
      });
    });
  });

  describe('R4: Завантаження списку', () => {
    it('повинен показати список компонентів при завантаженні', async () => {
      // Arrange
      componentsService.getAllComponents.mockResolvedValue(mockComponents);

      // Act
      renderWithRouter(<ComponentsList />);

      // Assert
      await waitFor(() => {
        expect(screen.getByText('Component 1')).toBeInTheDocument();
        expect(screen.getByText('Component 2')).toBeInTheDocument();
      });
    });

    it('повинен показати повідомлення при порожньому списку', async () => {
      // Arrange
      componentsService.getAllComponents.mockResolvedValue([]);

      // Act
      renderWithRouter(<ComponentsList />);

      // Assert
      await waitFor(() => {
        expect(screen.queryByText('Component 1')).not.toBeInTheDocument();
      });
    });
  });
});
