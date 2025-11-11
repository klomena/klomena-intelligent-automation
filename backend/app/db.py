"""
Database session management for the Klomena backend.

We use SQLAlchemy's engine + sessionmaker to keep things explicit and easy to
maintain. The declarative `Base` class is imported by the SQLAlchemy models.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import get_settings

settings = get_settings()

# echo=True in local mode prints SQL queries, which is helpful during debugging.
engine = create_engine(
    settings.database_url,
    echo=settings.app_env == "local",
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""


def get_db() -> Generator:
    """
    Provide a SQLAlchemy session to FastAPI path operations.

    FastAPI will automatically close the session when the request is complete.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
