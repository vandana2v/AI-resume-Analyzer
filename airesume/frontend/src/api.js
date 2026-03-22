import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const loginUser = (username, password) =>
  API.post("/login", { username, password });

export const registerUser = (username, password) =>
  API.post("/register", { username, password });

export const analyzeResume = (formData) =>
  API.post("/analyze", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });