import api from './api';

export const componentsService = {
  // Get all components
  getAll: async () => {
    const response = await api.get('/components/');
    return response.data;
  },

  // Get component by ID
  getById: async (id) => {
    const response = await api.get(`/components/${id}`);
    return response.data;
  },

  // Create new component
  create: async (data) => {
    const response = await api.post('/components/', data);
    return response.data;
  },

  // Update component
  update: async (id, data) => {
    const response = await api.put(`/components/${id}`, data);
    return response.data;
  },

  // Delete component
  delete: async (id) => {
    const response = await api.delete(`/components/${id}`);
    return response.data;
  }
};
