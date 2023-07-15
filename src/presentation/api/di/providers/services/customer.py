from typing import Annotated

from fastapi import Depends

from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer.interfaces.dao import CustomerDAO
from src.core.customer.services import CreateCustomerService, GetCustomerService
from src.presentation.api.di.stub import Stub


def get_customer_service(dao: CustomerDAO = Depends(Stub(CustomerDAO))) -> GetCustomerService:
    return GetCustomerService(dao=dao)


def create_customer_service(
    uow: Annotated[UoW, Depends(Stub(UoW))],
    dao: Annotated[UoW, Depends(Stub(CustomerDAO))]
) -> CreateCustomerService:
    return CreateCustomerService(uow=uow, dao=dao)