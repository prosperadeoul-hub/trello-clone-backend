from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker, create_async_engine)
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)

AsyncSessionLocal = async_sessionmaker(
    expire_on_commit = False,
    bind = engine,
    class_ = AsyncSession,
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session