from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

from app.core.config import settings

# Create the synchronous engine
engine = create_engine(settings.DATABASE_URL, pool_size=50, max_overflow=10)

# Create a session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# Base class for declarative models
Base = declarative_base()


# Dependency to provide a database session
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db
    finally:
        db.close()

