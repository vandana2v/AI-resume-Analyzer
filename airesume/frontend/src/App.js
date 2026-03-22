import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

import Login from "./components/Login";
import Register from "./components/Register";
import ResumeUpload from "./components/ResumeUpload";
import JobList from "./components/JobList";
import Navbar from "./components/Navbar";

import { getToken } from "./auth";

export default function App() {
  const isLoggedIn = getToken();

  return (
    <Router>
      {isLoggedIn && <Navbar />}

      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route
          path="/dashboard"
          element={isLoggedIn ? <ResumeUpload /> : <Navigate to="/login" />}
        />

        <Route
          path="/jobs"
          element={isLoggedIn ? <JobList /> : <Navigate to="/login" />}
        />
      </Routes>
    </Router>
  );
}