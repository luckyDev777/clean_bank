from src.core.account import dto_account
from src.core.account.interfaces.dao import AccountDAO
from src.core.common.exceptions.dao import DAOError
from src.core.common.interfaces.persistance.uow import UoW


class CreateAccountService:
    def __init__(self, dao: AccountDAO, uow: UoW) -> None:
        self._dao = dao
        self._uow = uow

    async def __call__(self, account_info: dto_account.CreateAccount) -> dto_account.Account:
        try:
            new_account = await self._dao.create_account(account_info=account_info)
        except DAOError as err:
            await self._uow.rollback()
            raise err

        await self._uow.commit()

        return new_account
