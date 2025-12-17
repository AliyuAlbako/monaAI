import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000/api/v1", // change if deployed
  headers: {
    "Content-Type": "application/json",
  },
});

export const sendMessage = async (prompt, sessionId) => {
  const payload = { prompt };

  if (sessionId) payload.session_id = sessionId;

  const res = await API.post("/generate", payload);
  return res.data;
};
