from sqlalchemy import select

from src.core.account import dto_account
from src.core.account.exceptions import AccountDoesNotExists
from src.core.account.interfaces.dao import AccountDAO

from ..converters import convert_account_model_to_dto
from ..exception_mapper import exception_mapper
from ..models import Account
from .base import SQLAlchemyDAO


class AccountDAOImpl(SQLAlchemyDAO, AccountDAO):
    @exception_mapper
    async def get_account_by_id(self, *, account_id: int) -> dto_account.Account:
        statement = select(Account).where(Account.id == account_id)
        account: Account | None = await self._session.scalar(statement=statement)
        if not account:
            raise AccountDoesNotExists(account_id=account_id)
        return convert_account_model_to_dto(account=account)

    @exception_mapper
    async def create_account(
        self, *, account_info: dto_account.CreateAccount
    ) -> dto_account.Account:
        new_account = Account(
            account_number=account_info.account_number,
            balance=account_info.balance,
            customer_id=account_info.customer_id
        )
        self._session.add(new_account)

        await self._session.flush()

        return convert_account_model_to_dto(new_account)
    
