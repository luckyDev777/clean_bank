from src.core.common.exceptions.dao import DAOError
from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer import dto
from src.core.customer.interfaces.dao import CustomerDAO


class UpdateCustomerService:
    def __init__(self, dao: CustomerDAO, uow: UoW) -> None:
        self._dao = dao
        self._uow = uow

    async def __call__(
        self, customer_id: int, customer_info: dto.UpdateCustomer
    ) -> dto.GetCustomer:
        try:
            updated_customer = await self._dao.update_customer(
                customer_id=customer_id, customer_info=customer_info
            )
        except DAOError as err:
            await self._uow.rollback()
            raise err

        await self._uow.commit()

        return updated_customer
