from typing import Protocol

from src.core.customer import dto


class CustomerDAO(Protocol):
    async def get_customers(self) -> list[dto.Customer]:
        ...

    async def get_customer_by_id(self, *, customer_id: int) -> dto.Customer:
        ...

    async def create_customer(
        self, *, customer_info: dto.CreateCustomer
    ) -> dto.Customer:
        ...

    async def update_customer(
        self, *, customer_id: int, customer_info: dto.UpdateCustomer
    ) -> dto.Customer:
        ...

    async def delete_customer(self, *, customer_id: int) -> None:
        ...
