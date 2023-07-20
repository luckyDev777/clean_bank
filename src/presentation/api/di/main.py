from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.core.account.interfaces.dao import AccountDAO
from src.core.account.services import (  # GetAllAccountsService,; UpdateAccountService,; DeleteAccountService,
    CreateAccountService,
    GetAccountService,
)
from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer.interfaces.dao import CustomerDAO
from src.core.customer.services import (
    CreateCustomerService,
    DeleteCustomerService,
    GetAllCustomers,
    GetCustomerService,
    UpdateCustomerService,
)

from ..settings.config import Config
from .providers.db.main import session_provider
from .providers.db.uow import account_dao_provider, customer_dao_provider, uow_provider
from .providers.services.account import create_account_service, get_account_service
from .providers.services.customer import (
    create_customer_service,
    delete_customer_service,
    get_all_customers_service,
    get_customer_service,
    update_customer_service,
)
from .stub import Stub


def setup_di(app: FastAPI, config: Config) -> None:
    # Setup DB dependencies
    app.dependency_overrides[Stub(AsyncEngine)] = lambda: app.state.engine
    app.dependency_overrides[
        Stub(async_sessionmaker[AsyncSession])
    ] = lambda: app.state.pool
    app.dependency_overrides[Stub(AsyncSession)] = session_provider
    app.dependency_overrides[Stub(UoW)] = uow_provider
    app.dependency_overrides[Stub(CustomerDAO)] = customer_dao_provider
    app.dependency_overrides[Stub(AccountDAO)] = account_dao_provider

    # Setup CustomerServices
    app.dependency_overrides[Stub(CreateCustomerService)] = create_customer_service
    app.dependency_overrides[Stub(GetCustomerService)] = get_customer_service
    app.dependency_overrides[Stub(GetAllCustomers)] = get_all_customers_service
    app.dependency_overrides[Stub(DeleteCustomerService)] = delete_customer_service
    app.dependency_overrides[Stub(UpdateCustomerService)] = update_customer_service

    # Setup AccountServices
    app.dependency_overrides[Stub(CreateAccountService)] = create_account_service
    app.dependency_overrides[Stub(GetAccountService)] = get_account_service
