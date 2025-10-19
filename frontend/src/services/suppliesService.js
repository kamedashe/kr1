import api from './api';

export const suppliesService = {
  // Get all supplies
  getAll: async () => {
    const response = await api.get('/supplies/');
    return response.data;
  },

  // Create new supply
  create: async (data) => {
    const response = await api.post('/supplies/', data);
    return response.data;
  },

  // Delete supply
  delete: async (id) => {
    const response = await api.delete(`/supplies/${id}`);
    return response.data;
  }
};
