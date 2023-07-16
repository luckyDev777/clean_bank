from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.core.customer import dto
from src.core.customer.exceptions import CustomerDoesNotExists
from .base import SQLAlchemyDAO
from src.core.customer.interfaces.dao import CustomerDAO
from ..converters import convert_customer_models_to_dto
from ..exception_mapper import exception_mapper
from ..models import Customer, Account


class CustomerDAOImpl(SQLAlchemyDAO, CustomerDAO):

    @exception_mapper
    async def get_customer_by_id(self, *, customer_id: int) -> dto.Customer:
        statement = select(Customer).where(Customer.id == customer_id)
        # statement = select(Customer).options(joinedload(Customer.accounts)).where(Customer.id == customer_id)
        customer: Customer | None = await self._session.scalar(statement=statement)
        if not customer:
            raise CustomerDoesNotExists(customer_id=customer_id)
        return convert_customer_models_to_dto(customer=customer)
    
    @exception_mapper
    async def create_customer(self, *, customer_info: dto.CreateCustomer) -> dto.Customer:
        new_customer = Customer(
            name=customer_info.name,
            email=customer_info.email,
            phone_number=customer_info.phone_number
        )
        self._session.add(new_customer)

        await self._session.flush()

        return convert_customer_models_to_dto(customer=new_customer)