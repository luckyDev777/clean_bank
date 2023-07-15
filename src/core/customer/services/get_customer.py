from typing import Any
from src.core.customer import dto
from src.core.customer.interfaces.dao import CustomerDAO


class GetCustomerService:
    def __init__(self, dao: CustomerDAO) -> None:
        self._dao = dao

    async def __call__(self, customer_info: dto.GetCustomer) -> dto.Customer:
        customer = await self._dao.get_customer_by_id(customer_id=customer_info.customer_id)
        return customer