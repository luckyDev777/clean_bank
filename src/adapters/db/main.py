import contextlib
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession

from .config import DBConfig



def create_engine(db_config: DBConfig) -> AsyncEngine:
    return create_async_engine(url=db_config.full_url, echo=db_config.db_echo)



def session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncEngine]:
    return async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


@contextlib.asynccontextmanager
async def build_session(
    factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with factory() as session:
        yield session