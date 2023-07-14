from dataclasses import dataclass

from src.core.common.exceptions.base import AppException


@dataclass
class CustomerDoesNotExists(AppException):
    customer_id: int

    @property
    def message(self) -> str:
        return f"Customer with {self.customer_id} does not exists"