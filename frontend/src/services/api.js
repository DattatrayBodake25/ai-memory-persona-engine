import axios from "axios";
import { API_BASE_URL } from "./config";

export const extractMemory = async (messages) => {
  const res = await axios.post(`${API_BASE_URL}/memory/extract`, {
    messages
  });
  return res.data;
};

export const getAllMemory = async () => {
  const res = await axios.get(`${API_BASE_URL}/memory/all`);
  return res.data;
};

export const transformPersona = async (message, persona) => {
  const res = await axios.post(`${API_BASE_URL}/persona/transform`, {
    message,
    persona
  });
  return res.data;
};
