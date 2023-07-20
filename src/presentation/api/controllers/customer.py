from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from src.core.customer import dto_customer
from src.core.customer.exceptions import CustomerDoesNotExists
from src.core.customer.services.create_customer import CreateCustomerService
from src.core.customer.services.delete_customer import DeleteCustomerService
from src.core.customer.services.get_all_customers import GetAllCustomers
from src.core.customer.services.get_customer import GetCustomerService
from src.core.customer.services.update_customer import UpdateCustomerService
from src.presentation.api.controllers.responses import ErrorResult
from src.presentation.api.di.stub import Stub

router = APIRouter(prefix="/customers", tags=["customers"])


@router.get(
    path="/",
    responses={
        status.HTTP_200_OK: {"model": list[dto_customer.Customer]},
    },
)
async def get_customers(
    service: Annotated[GetAllCustomers, Depends(Stub(GetAllCustomers))]
) -> list[dto_customer.Customer]:
    return await service()


@router.get(
    path="/{customer_id}",
    responses={
        status.HTTP_200_OK: {"model": dto_customer.Customer},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[CustomerDoesNotExists]},
    },
)
async def get_customer_by_id(
    customer_id: int,
    service: Annotated[GetCustomerService, Depends(Stub(GetCustomerService))],
) -> dto_customer.Customer:
    return await service(dto_customer.GetCustomer(customer_id=customer_id))


@router.post(
    path="/create", responses={status.HTTP_201_CREATED: {"model": dto_customer.Customer}}
)
async def create_customer(
    customer_info: dto_customer.CreateCustomer,
    service: Annotated[CreateCustomerService, Depends(Stub(CreateCustomerService))],
) -> dto_customer.Customer:
    return await service(customer_info=customer_info)


@router.put(
    path="/{customer_id}",
    responses={
        status.HTTP_201_CREATED: {"model": dto_customer.Customer},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[CustomerDoesNotExists]},
    },
)
async def update_customer(
    customer_id: int,
    customer_info: dto_customer.UpdateCustomer,
    service: Annotated[UpdateCustomerService, Depends(Stub(UpdateCustomerService))],
) -> dto_customer.Customer:
    return await service(customer_id=customer_id, customer_info=customer_info)


@router.delete(
    path="/{customer_id}",
    responses={
        status.HTTP_204_NO_CONTENT: {"model": None},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[CustomerDoesNotExists]},
    },
)
async def delete_customer(
    customer_id: int,
    service: Annotated[DeleteCustomerService, Depends(Stub(DeleteCustomerService))],
) -> None:
    await service(customer_id=customer_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
