from dataclasses import dataclass

from src.core.common.dto.base import DTO


@dataclass(frozen=True)
class Customer(DTO):
    customer_id: int
    name: str
    email: str
    phone_number: str