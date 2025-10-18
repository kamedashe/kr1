import api from './api';

export const suppliersService = {
  // Get all suppliers
  getAll: async () => {
    const response = await api.get('/suppliers/');
    return response.data;
  },

  // Get supplier by ID
  getById: async (id) => {
    const response = await api.get(`/suppliers/${id}`);
    return response.data;
  },

  // Create new supplier
  create: async (data) => {
    const response = await api.post('/suppliers/', data);
    return response.data;
  },

  // Update supplier
  update: async (id, data) => {
    const response = await api.put(`/suppliers/${id}`, data);
    return response.data;
  },

  // Delete supplier
  delete: async (id) => {
    const response = await api.delete(`/suppliers/${id}`);
    return response.data;
  }
};
