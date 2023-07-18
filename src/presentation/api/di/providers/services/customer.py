from typing import Annotated

from fastapi import Depends

from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer.interfaces.dao import CustomerDAO
from src.core.customer.services import (
    CreateCustomerService,
    DeleteCustomerService,
    GetAllCustomers,
    GetCustomerService,
    UpdateCustomerService,
)
from src.presentation.api.di.stub import Stub


def get_all_customers_service(
    dao: CustomerDAO = Depends(Stub(CustomerDAO)),
) -> GetAllCustomers:
    return GetAllCustomers(dao=dao)


def get_customer_service(
    dao: CustomerDAO = Depends(Stub(CustomerDAO)),
) -> GetCustomerService:
    return GetCustomerService(dao=dao)


def create_customer_service(
    dao: Annotated[CustomerDAO, Depends(Stub(CustomerDAO))],
    uow: Annotated[UoW, Depends(Stub(UoW))],
) -> CreateCustomerService:
    return CreateCustomerService(dao=dao, uow=uow)


def update_customer_service(
    dao: Annotated[CustomerDAO, Depends(Stub(CustomerDAO))],
    uow: Annotated[UoW, Depends(Stub(UoW))],
) -> UpdateCustomerService:
    return UpdateCustomerService(dao=dao, uow=uow)


def delete_customer_service(
    dao: Annotated[CustomerDAO, Depends(Stub(CustomerDAO))],
    uow: Annotated[UoW, Depends(Stub(UoW))],
) -> DeleteCustomerService:
    return DeleteCustomerService(dao=dao, uow=uow)
