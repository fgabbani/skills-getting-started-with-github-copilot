const API_BASE = "";

export async function login(email, password) {
  const res = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || "Login failed");
  }
  const data = await res.json();
  sessionStorage.setItem("token", data.access_token);
  return data;
}

export async function getMe() {
  const token = sessionStorage.getItem("token");
  const res = await fetch(`${API_BASE}/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error("Unauthorized");
  return res.json();
}

export function logout() {
  sessionStorage.removeItem("token");
}

export function isAuthenticated() {
  return !!sessionStorage.getItem("token");
}
