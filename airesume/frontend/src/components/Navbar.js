import React from "react";
import { useNavigate } from "react-router-dom";
import { logout } from "../auth";

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
    window.location.reload();
  };

  return (
    <div style={{ padding: "12px", background: "#222", color: "#fff", display: "flex", gap: "10px" }}>
      <h2 style={{ marginRight: "20px" }}>AI Resume Analyzer</h2>
      <button onClick={() => navigate("/dashboard")}>Dashboard</button>
      <button onClick={() => navigate("/jobs")}>Jobs</button>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}