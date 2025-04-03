import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      alert("Access Denied! Please Login.");
      navigate("/login");
    }
  }, [navigate]);

  return <h1>Welcome to your Dashboard</h1>;
}

export default Dashboard;
