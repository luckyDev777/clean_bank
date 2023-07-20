from src.core.account import dto_account
from src.core.account.interfaces.dao import AccountDAO


class GetAccountService:
    def __init__(self, dao: AccountDAO) -> None:
        self._dao = dao

    async def __call__(self, account_info: dto_account.GetAccount) -> dto_account.Account:
        account = await self._dao.get_account_by_id(
            account_id=account_info.account_id
        )
        return account
