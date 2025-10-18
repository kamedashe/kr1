import api from './api';

export const storekeepersService = {
  // Get all storekeepers
  getAll: async () => {
    const response = await api.get('/storekeepers/');
    return response.data;
  },

  // Get storekeeper by ID
  getById: async (id) => {
    const response = await api.get(`/storekeepers/${id}`);
    return response.data;
  },

  // Create new storekeeper
  create: async (data) => {
    const response = await api.post('/storekeepers/', data);
    return response.data;
  },

  // Update storekeeper
  update: async (id, data) => {
    const response = await api.put(`/storekeepers/${id}`, data);
    return response.data;
  },

  // Delete storekeeper
  delete: async (id) => {
    const response = await api.delete(`/storekeepers/${id}`);
    return response.data;
  }
};
