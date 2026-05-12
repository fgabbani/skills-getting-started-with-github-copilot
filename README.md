# Mergington High School Management System

A web application for viewing and signing up for extracurricular activities at Mergington High School.

## Architecture

- **Backend:** FastAPI (Python) — REST API with JWT authentication
- **Frontend:** React — Single-page application with login and activity management

## Backend Setup

```bash
pip install -r requirements.txt
uvicorn src.app:app --reload
```

The API runs on `http://localhost:8000`.

## Frontend Setup

```bash
cd frontend
npm install
npm start
```

The frontend runs on `http://localhost:3000` and proxies API calls to the backend.

## Available Users

| Email                      | Password      |
|----------------------------|---------------|
| michael@mergington.edu     | password123   |
| emma@mergington.edu        | password123   |
| john@mergington.edu        | password123   |

## API Endpoints

| Method | Path                                      | Description                  |
|--------|-------------------------------------------|------------------------------|
| POST   | `/login`                                  | Authenticate and get JWT     |
| GET    | `/me`                                     | Get current user info        |
| GET    | `/activities`                             | List all activities          |
| POST   | `/activities/{name}/signup?email=...`     | Sign up for an activity      |
| DELETE | `/activities/{name}/participants?email=...`| Unregister from an activity  |

