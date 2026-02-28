from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base
from app.api.dependencies import get_db
from app.main import app

# In-memory SQLite shared across connections
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Create tables once for test engine
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_lead_success():
    payload = {
        "full_name": "John Doe",
        "email": "john@example.com",
        "company": "Test Inc",
        "message": "Interested",
        "source": "landing-page",
    }

    response = client.post("/leads", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == payload["email"]


def test_create_lead_duplicate():
    payload = {
        "full_name": "Jane Doe",
        "email": "duplicate@example.com",
        "company": "Test Inc",
        "message": "Interested",
        "source": "landing-page",
    }

    response1 = client.post("/leads", json=payload)
    assert response1.status_code == 201

    response2 = client.post("/leads", json=payload)
    assert response2.status_code == 409