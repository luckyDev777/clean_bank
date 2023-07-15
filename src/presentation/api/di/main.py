from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine

from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer.interfaces.dao import CustomerDAO
from src.core.customer.services import CreateCustomerService, GetCustomerService
from .providers.db.uow import uow_provider, customer_dao_provider
from .providers.db.main import session_provider
from .providers.services.customer import get_customer_service, create_customer_service
from .stub import Stub
from ..settings.config import Config


def setup_di(app: FastAPI) -> None:
    # Setup DB dependencies
    app.dependency_overrides[Stub(AsyncEngine)] = lambda: app.state.engine
    app.dependency_overrides[Stub(async_sessionmaker[AsyncSession])] = lambda: app.state.pool
    app.dependency_overrides[Stub(AsyncEngine)] = session_provider
    app.dependency_overrides[Stub(UoW)] = uow_provider
    app.dependency_overrides[Stub(CustomerDAO)] = customer_dao_provider

    # Setup services
    app.dependency_overrides[Stub(CreateCustomerService)] = create_customer_service
    app.dependency_overrides[Stub(GetCustomerService)] = get_customer_service