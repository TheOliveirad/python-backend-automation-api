# python-backend-automation-api

Production-oriented FastAPI backend showcasing clean architecture, validation, service separation, logging, Docker, and tests.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Python Backend Automation API

Production-ready FastAPI backend demonstrating:

- Layered architecture (routes → services → models)
- SQLAlchemy 2.0 ORM
- Business rule enforcement (unique email constraint)
- Proper HTTP semantics (201, 409)
- Deterministic automated tests
- In-memory database isolation for testing
- Dockerized deployment
- OpenAPI documentation

---

## Architecture

app/
- api/ → HTTP layer
- services/ → business logic
- models/ → ORM models
- schemas.py → Pydantic validation
- database.py → SQLAlchemy engine/session
- config.py → environment configuration

---

## Features

- Create lead (POST /leads)
- List leads (GET /leads)
- Unique email validation
- Proper conflict handling (409)
- Health endpoint (GET /health)

---

## Run Locally
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Open:

http://localhost:8000/docs

---

## Run with Docker
docker compose build
docker compose up


Open:

http://localhost:8000/docs

---

## Testing
python -m pytest


Tests use an isolated in-memory SQLite database with StaticPool to ensure deterministic behavior.

---

## Tech Stack

- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- SQLite
- Pytest
- Docker