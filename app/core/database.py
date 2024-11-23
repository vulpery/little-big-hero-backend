from contextlib import asynccontextmanager
from functools import wraps
from inspect import signature

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

async_engine = create_async_engine(settings.DATABASE_URL, pool_size=50, max_overflow=10)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

Base = declarative_base()

@asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


def with_db(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        func_signature = signature(func)
        parameters = func_signature.parameters

        if "db" in kwargs:
            return await func(*args, **kwargs)

        if "db" in parameters:
            db_index = list(parameters).index("db")
            if len(args) > db_index:
                return func(*args, **kwargs)

        async with get_db():
            return await func(*args, **kwargs)

    return wrapper
