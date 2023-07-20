from dataclasses import dataclass

from src.core.common.exceptions.base import AppException


@dataclass
class AccountDoesNotExists(AppException):
    account_id: int

    @property
    def message(self) -> str:
        return f"Account with {self.account_id} does not exists"
