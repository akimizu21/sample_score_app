import axios from "axios";

// 環境に応じてベースURLを自動判定
const getBaseURL = () => {
  if (process.env.NODE_ENV === "production") {
    return "https://manavis-api.onrender.com/api"; // 実際のURLに変更
  }
  return "http://localhost:5000/api";
};

const axiosClient = axios.create({
  baseURL: getBaseURL(),
  headers: { "Content-Type": "application/json" },
});

export default axiosClient;