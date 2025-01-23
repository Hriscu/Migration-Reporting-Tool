import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1/identity/';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
});

const saveTokens = (access, refresh) => {
  localStorage.setItem('accessToken', access);
  localStorage.setItem('refreshToken', refresh);
};

export const getAccessToken = () => localStorage.getItem('accessToken');
export const getRefreshToken = () => localStorage.getItem('refreshToken');

export const removeTokens = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
};

export const login = async (email, password) => {
  try {
    const response = await apiClient.post('login/', { email, password });
    saveTokens(response.data.access, response.data.refresh);
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

export const register = async (firstName, lastName, email, password) => {
  try {
    const role = 'USER';
    const response = await apiClient.post('register/', {
      first_name: firstName,
      last_name: lastName,
      email,
      password,
      role,
    });
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

export const refresh = async () => {
  try {
    const refresh = getRefreshToken();
    const response = await apiClient.post('refresh/', { refresh });
    saveTokens(response.data.access, refresh);
    return response.data.access;
  } catch (error) {
    removeTokens();
    throw error.response?.data || error.message;
  }
};
