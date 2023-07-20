from src.core.customer import dto_customer
from src.core.customer.interfaces.dao import CustomerDAO


class GetCustomerService:
    def __init__(self, dao: CustomerDAO) -> None:
        self._dao = dao

    async def __call__(self, customer_info: dto_customer.GetCustomer) -> dto_customer.Customer:
        customer = await self._dao.get_customer_by_id(
            customer_id=customer_info.customer_id
        )
        return customer
