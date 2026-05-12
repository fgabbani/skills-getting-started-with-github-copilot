"""Tests for the login and authentication endpoints."""


def test_login_success(client):
    response = client.post("/login", json={"email": "michael@mergington.edu", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    response = client.post("/login", json={"email": "michael@mergington.edu", "password": "wrong"})
    assert response.status_code == 401


def test_login_unknown_user(client):
    response = client.post("/login", json={"email": "unknown@mergington.edu", "password": "password123"})
    assert response.status_code == 401
