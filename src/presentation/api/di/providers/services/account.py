from typing import Annotated

from fastapi import Depends

from src.core.common.interfaces.persistance.uow import UoW
from src.core.account.interfaces.dao import AccountDAO
from src.core.account.services import (
    CreateAccountService, 
    GetAccountService
)
from src.presentation.api.di.stub import Stub


def get_account_service(
    dao: AccountDAO = Depends(Stub(AccountDAO))
) -> GetAccountService:
    return GetAccountService(dao=dao)


def create_account_service(
    dao: Annotated[AccountDAO, Depends(Stub(AccountDAO))],
    uow: Annotated[UoW, Depends(Stub(UoW))]
) -> CreateAccountService:
    return CreateAccountService(dao=dao, uow=uow)