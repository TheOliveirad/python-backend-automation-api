# python-backend-automation-api

Production-ready FastAPI backend demonstrating layered architecture,\
database integrity rules, service-layer abstraction, deterministic
testing,\
and containerized deployment.

This repository showcases production-oriented backend engineering
practices rather than tutorial-style CRUD scaffolding.

------------------------------------------------------------------------

## Overview

This project implements a **Lead Capture & Processing API** with:

-   Layered routing → service → persistence architecture\
-   Pydantic v2 request/response validation\
-   SQLAlchemy 2.0 ORM integration\
-   Database-level uniqueness constraint enforcement\
-   Proper HTTP semantics (201, 409)\
-   Structured application logging\
-   Environment-driven configuration\
-   Deterministic in-memory database testing\
-   Dockerized deployment

The goal is to demonstrate clean backend design suitable for real-world
API and automation systems.

------------------------------------------------------------------------

## Architecture

### Layered Flow

``` mermaid
flowchart TD
    A[Client] -->|HTTP| B[FastAPI Routes]
    B --> C[Service Layer]
    C --> D[SQLAlchemy ORM]
    D --> E[(SQLite Database)]
```

### Project Structure

    app/
     ├── main.py              # Application entrypoint
     ├── api/
     │    ├── routes/         # API endpoint modules
     │    └── dependencies.py # Dependency injection
     ├── services/            # Business logic layer
     ├── models/              # SQLAlchemy ORM models
     ├── schemas.py           # Pydantic request/response models
     ├── database.py          # Engine + session management
     ├── config.py            # Environment configuration
     ├── logger.py            # Structured logging config
    tests/                    # Pytest test suite
    Dockerfile                # Container image
    docker-compose.yml        # Local orchestration

------------------------------------------------------------------------

## API Endpoints

### Health Check

`GET /health`

``` json
{
  "status": "ok"
}
```

------------------------------------------------------------------------

### Create Lead

`POST /leads`

Request:

``` json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "company": "Example Inc",
  "message": "Interested in product",
  "source": "landing-page"
}
```

Response (201):

``` json
{
  "id": 1,
  "full_name": "John Doe",
  "email": "john@example.com",
  "company": "Example Inc",
  "message": "Interested in product",
  "source": "landing-page",
  "created_at": "2026-02-28T10:00:00Z"
}
```

Duplicate email returns:

409 Conflict

``` json
{
  "detail": "Lead with this email already exists."
}
```

------------------------------------------------------------------------

### List Leads

`GET /leads`

Returns:

``` json
{
  "total": 1,
  "items": []
}
```

Supports:

-   `limit`
-   `offset`

------------------------------------------------------------------------

## Running Locally

``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Running with Docker

``` bash
docker compose up --build
```

Application runs at:

http://localhost:8000/docs

------------------------------------------------------------------------

## Testing

``` bash
pytest
```

Tests include:

-   Health endpoint validation\
-   Lead creation success case\
-   Duplicate email conflict handling\
-   Isolated in-memory SQLite engine using StaticPool

------------------------------------------------------------------------

## Environment Configuration

Example `.env`:

    DATABASE_URL=sqlite:///./app.db
    ENV=local
    LOG_LEVEL=INFO

`.env.example` documents expected keys.

------------------------------------------------------------------------

## Tech Stack

-   Python 3.12\
-   FastAPI\
-   SQLAlchemy 2.0\
-   Pydantic v2\
-   SQLite\
-   Pytest\
-   Docker

------------------------------------------------------------------------

## Purpose

This repository is part of a backend engineering portfolio focused on:

-   Automation systems\
-   Clean API architecture\
-   Production-oriented Python services\
-   Scalable layered application design
