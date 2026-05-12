import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getMe, logout } from "../services/auth";
import "./Welcome.css";

function Welcome() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    getMe()
      .then(setUser)
      .catch(() => {
        logout();
        navigate("/login");
      });
  }, [navigate]);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  if (!user) return <div className="loading">Loading...</div>;

  return (
    <div className="welcome-page">
      <header className="header">
        <h1>Mergington High School</h1>
        <button onClick={handleLogout}>Sign Out</button>
      </header>
      <main className="content">
        <div className="greeting-card">
          <h2>Welcome, {user.name}!</h2>
          <p>You are signed in as <strong>{user.email}</strong></p>
        </div>
      </main>
    </div>
  );
}

export default Welcome;
