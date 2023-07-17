from src.core.common.exceptions.dao import DAOError
from src.core.common.interfaces.persistance.uow import UoW
from src.core.customer.interfaces.dao import CustomerDAO


class DeleteCustomerService:
    def __init__(self, dao: CustomerDAO, uow: UoW) -> None:
        self._dao = dao
        self._uow = uow

    async def __call__(self, customer_id: int) -> None:
        try:
            await self._dao.delete_customer(customer_id=customer_id)
        except DAOError as err:
            await self._uow.rollback()
            raise err
        
        await self._uow.commit()

        return None