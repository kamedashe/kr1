import api from './api';

export const ordersService = {
  // Get all orders
  getAll: async () => {
    const response = await api.get('/orders/');
    return response.data;
  },

  // Create new order
  create: async (data) => {
    const response = await api.post('/orders/', data);
    return response.data;
  },

  // Delete order
  delete: async (id) => {
    const response = await api.delete(`/orders/${id}`);
    return response.data;
  }
};
