from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.core.account import dto_account
from src.core.account.exceptions import AccountDoesNotExists
from src.core.account.services.create_account import CreateAccountService
from src.core.account.services.get_account import GetAccountService
from src.presentation.api.controllers.responses.exceptions import ErrorResult
from src.presentation.api.di.stub import Stub


router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get(
    path="/{account_id}",
    responses={
        status.HTTP_200_OK: {"model": dto_account.Account},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[AccountDoesNotExists]},
    },
)
async def get_account_by_id(
    account_id: int,
    service: Annotated[GetAccountService, Depends(Stub(GetAccountService))],
) -> dto_account.Account:
    return await service(dto_account.GetAccount(account_id=account_id))


@router.post(
    path="/create",
    responses={
        status.HTTP_201_CREATED: {"model": dto_account.Account}
    }
)
async def create_account(
    account_info: dto_account.CreateAccount,
    service: Annotated[CreateAccountService, Depends(Stub(CreateAccountService))],
) -> dto_account.Account:
    return await service(account_info=account_info)