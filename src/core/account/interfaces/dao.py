from typing import Protocol

from src.core.account import dto_account


class AccountDAO(Protocol):
    # async def get_accounts(self) -> list[dto_account.Account]:
    #     ...

    async def get_account_by_id(self, *, account_id: int) -> dto_account.Account:
        ...

    async def create_account(
        self, *, account_info: dto_account.CreateAccount
    ) -> dto_account.Account:
        ...

    # async def update_account(
    #     self, *, account_id: int, account_info: dto_account.UpdateAccount
    # ) -> dto_account.Account:
    #     ...

    # async def delete_account(self, *, account_id: int) -> None:
    #     ...
