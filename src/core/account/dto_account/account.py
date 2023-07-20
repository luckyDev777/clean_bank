from dataclasses import dataclass

from src.core.common.dto.base import DTO


@dataclass(frozen=True)
class Account(DTO):
    account_id: int
    account_number: str
    balance: int
    customer_id: int


@dataclass(frozen=True)
class GetAccount(DTO):
    account_id: int


@dataclass(frozen=True)
class CreateAccount(DTO):
    account_number: str
    balance: int
    customer_id: int


@dataclass(frozen=True)
class UpdateAccount(DTO):
    account_number: str
    balance: int
    customer_id: int
