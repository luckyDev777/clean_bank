from sqlalchemy.ext.asyncio import AsyncSession

from src.core.common.interfaces.persistance.uow import UoW


class SQLAlchemyUoW(UoW):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
