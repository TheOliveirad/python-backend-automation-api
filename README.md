# python-backend-automation-api

Production-ready FastAPI backend demonstrating layered architecture,
validation, service abstraction, database integration, testing, and
containerized deployment.

This repository is designed to showcase backend engineering practices
suitable for real-world API systems and automation workflows.

------------------------------------------------------------------------

## Overview

This project implements a **Lead Capture & Processing API** with:

-   Modular routing
-   Pydantic request/response validation
-   Service layer abstraction
-   Database integration
-   Centralized configuration management
-   Structured logging
-   Dockerized deployment
-   Automated test coverage

The goal is to demonstrate production-oriented backend architecture
rather than a tutorial-style implementation.

------------------------------------------------------------------------

## Architecture

    app/
     ├── main.py              # Application entrypoint
     ├── api/
     │    ├── routes/         # API endpoint modules
     │    └── dependencies.py # Dependency injection
     ├── services/            # Business logic layer
     ├── models/              # Database models
     ├── schemas.py           # Pydantic validation schemas
     ├── database.py          # Database setup and session management
     ├── config.py            # Environment configuration
     ├── logger.py            # Centralized logging setup
    tests/                    # Pytest test suite
    Dockerfile                # Container build config
    docker-compose.yml        # Local orchestration

### Design Principles

-   Clear separation between routing and business logic
-   Explicit dependency management
-   Configurable via environment variables
-   Ready for containerized environments
-   Test-driven endpoint verification

------------------------------------------------------------------------

## API Endpoints

### Health Check

`GET /health`

Response:

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
  "name": "John Doe",
  "email": "john@example.com"
}
```

Response:

``` json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

------------------------------------------------------------------------

### List Leads

`GET /leads`

Returns all stored leads.

------------------------------------------------------------------------

## Running Locally

Create virtual environment:

    python -m venv .venv
    source .venv/bin/activate    # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

Run application:

    uvicorn app.main:app --reload

Open:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Running with Docker

Build and start:

    docker compose up --build

Application runs at:

    http://localhost:8000

------------------------------------------------------------------------

## Testing

Run tests with:

    pytest

Tests cover:

-   Health endpoint
-   Lead creation
-   Lead retrieval

------------------------------------------------------------------------

## Environment Configuration

Environment variables can be configured via `.env` file.

Example:

    DATABASE_URL=sqlite:///./test.db
    APP_ENV=development

A `.env.example` file documents expected configuration keys.

------------------------------------------------------------------------

## Future Improvements

-   Pagination and filtering for `/leads`
-   Authentication layer (JWT or API key)
-   Async database driver support
-   CI pipeline integration
-   Extended test coverage
-   Production logging configuration

------------------------------------------------------------------------

## Tech Stack

-   Python 3.12
-   FastAPI
-   Pydantic
-   SQLAlchemy (if used)
-   Pytest
-   Docker

------------------------------------------------------------------------

## Purpose

This repository is part of a curated backend engineering portfolio
focused on:

-   Automation systems
-   API architecture
-   Production-ready Python services
-   Scalable application structure
