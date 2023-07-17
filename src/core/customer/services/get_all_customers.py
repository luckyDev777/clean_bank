from src.core.customer import dto
from src.core.customer.interfaces.dao import CustomerDAO


class GetAllCustomers:
    def __init__(self, dao: CustomerDAO) -> None:
        self._dao = dao

    async def __call__(self) -> list[dto.Customer]:
        customers = await self._dao.get_customers()
        return customers
