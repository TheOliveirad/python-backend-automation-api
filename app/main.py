from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import health_router, leads_router
from app.config import settings
from app.database import Base, engine
from app.logger import configure_logging, get_logger


configure_logging(settings.log_level)
log = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle management.

    Handles startup and shutdown events using modern FastAPI lifespan API.
    """
    log.info(f"startup env={settings.env}")
    yield
    log.info("shutdown")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        lifespan=lifespan,
    )

    # Create tables on startup (v1 approach; replace with migrations later)
    Base.metadata.create_all(bind=engine)

    app.include_router(health_router)
    app.include_router(leads_router)

    return app


app = create_app()