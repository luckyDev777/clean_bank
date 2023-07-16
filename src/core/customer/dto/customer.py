from dataclasses import dataclass

from src.core.common.dto.base import DTO


@dataclass(frozen=True)
class Customer(DTO):
    customer_id: int
    name: str
    email: str
    phone_number: str
    accounts: list


@dataclass(frozen=True)
class GetCustomer(DTO):
    customer_id: int


@dataclass
class CreateCustomer(DTO):
    name: str
    email: str
    phone_number: str


@dataclass
class UpdateCustomer(DTO):
    name: str
    email: str
    phone_number: str