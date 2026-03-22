import React, { useState } from "react";
import { analyzeResume } from "../api";
import JobList from "./JobList";

export default function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const upload = async () => {
    if (!file) {
      setError("Please select a file first");
      return;
    }

    try {
      setError("");
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const res = await analyzeResume(formData);

      setJobs(res.data.jobs || []);
    } catch (err) {
      setError("Failed to analyze resume");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>📄 Upload Resume</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={upload} style={{ marginTop: "10px" }}>
        Analyze Resume
      </button>

      {loading && <p style={{ marginTop: "10px" }}>⏳ Analyzing...</p>}

      {error && (
        <p style={{ color: "red", marginTop: "10px" }}>{error}</p>
      )}

      {jobs.length > 0 && (
        <div style={{ marginTop: "20px" }}>
          <h3>🎯 Matched Jobs</h3>
          <JobList jobs={jobs} />
        </div>
      )}
    </div>
  );
}