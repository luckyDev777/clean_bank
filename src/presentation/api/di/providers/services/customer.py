from typing import Annotated

from fastapi import Depends

from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer.interfaces.dao import CustomerDAO
from src.core.customer.services import (CreateCustomerService,
                                        DeleteCustomerService, GetAllCustomers,
                                        GetCustomerService,
                                        UpdateCustomerService)
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
    uow: Annotated[UoW, Depends(Stub(UoW))],
    dao: Annotated[UoW, Depends(Stub(CustomerDAO))],
) -> CreateCustomerService:
    return CreateCustomerService(uow=uow, dao=dao)


def update_customer_service(
    uow: Annotated[UoW, Depends(Stub(UoW))],
    dao: Annotated[UoW, Depends(Stub(CustomerDAO))],
) -> UpdateCustomerService:
    return UpdateCustomerService(uow=uow, dao=dao)


def delete_customer_service(
    uow: Annotated[UoW, Depends(Stub(UoW))],
    dao: Annotated[UoW, Depends(Stub(CustomerDAO))],
) -> DeleteCustomerService:
    return DeleteCustomerService(uow=uow, dao=dao)
