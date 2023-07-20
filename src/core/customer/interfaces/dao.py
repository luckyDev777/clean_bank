from typing import Protocol

from src.core.customer import dto_customer


class CustomerDAO(Protocol):
    async def get_customers(self) -> list[dto_customer.Customer]:
        ...

    async def get_customer_by_id(self, *, customer_id: int) -> dto_customer.Customer:
        ...

    async def create_customer(
        self, *, customer_info: dto_customer.CreateCustomer
    ) -> dto_customer.Customer:
        ...

    async def update_customer(
        self, *, customer_id: int, customer_info: dto_customer.UpdateCustomer
    ) -> dto_customer.Customer:
        ...

    async def delete_customer(self, *, customer_id: int) -> None:
        ...
