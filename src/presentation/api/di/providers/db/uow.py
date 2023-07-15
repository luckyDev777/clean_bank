from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.db.dao.customer import CustomerDAOImpl
from src.adapters.db.uow import SQLAlchemyUoW
from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer.interfaces.dao import CustomerDAO
from src.presentation.api.di.stub import Stub


def uow_provider(session: Annotated[AsyncSession, Depends(Stub(AsyncSession))]) -> UoW:
    return SQLAlchemyUoW(session=session)


def customer_dao_provider(session: Annotated[AsyncSession, Depends(Stub(AsyncSession))]) -> CustomerDAO:
    return CustomerDAOImpl(session=session)