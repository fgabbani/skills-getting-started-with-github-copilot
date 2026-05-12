# Backend JWT API

API REST construida con **FastAPI** que implementa autenticación basada en **JWT** (JSON Web Tokens).

## Características

- Endpoint de login (`POST /token`) que recibe usuario y contraseña y devuelve un JWT con expiración de 300 segundos.
- Endpoint de refresh (`POST /token/refresh`) que recibe un token válido y devuelve uno nuevo.
- Gestión de dependencias con **Poetry**.
- Despliegue con **Docker** y **Docker Compose**.

## Credenciales por defecto

| Usuario | Contraseña |
|---------|------------|
| admin   | admin123   |

## Requisitos

- Python 3.11+
- [Poetry](https://python-poetry.org/)
- Docker y Docker Compose (opcional, para despliegue con contenedores)

## Instalación local

```bash
cd backend
poetry install
```

## Ejecución local

```bash
poetry run uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`.

## Ejecución con Docker

```bash
cd backend
docker compose up --build
```

La API estará disponible en `http://localhost:8000`.

## Uso

### Obtener un token

```bash
curl -X POST http://localhost:8000/token \
  -d "username=admin&password=admin123"
```

Respuesta:

```json
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}
```

### Refrescar un token

```bash
curl -X POST http://localhost:8000/token/refresh \
  -H "Authorization: Bearer <JWT>"
```

Respuesta:

```json
{
  "access_token": "<NEW_JWT>",
  "token_type": "bearer"
}
```

### Documentación interactiva

FastAPI genera documentación automática disponible en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
