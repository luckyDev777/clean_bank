from typing import Annotated
from fastapi import APIRouter, Response, status, Depends

from src.core.customer import dto
from src.core.customer.services.create_customer import CreateCustomerService
from src.core.customer.services.get_customer import GetCustomerService

from src.presentation.api.di.stub import Stub
from src.presentation.api.controllers.responses import ErrorResult
from src.core.customer.exceptions import CustomerDoesNotExists


router = APIRouter(prefix="/customers", tags=["customers"])


@router.get(
    path="/{customer_id}",
    responses={
        status.HTTP_200_OK: {"model": dto.Customer},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResult[CustomerDoesNotExists]},
    },
)
async def get_customer_by_id(
    customer_id: int,
    service: Annotated[GetCustomerService, Depends(Stub(GetCustomerService))]
) -> dto.Customer:
    return await service(dto.GetCustomer(customer_id=customer_id))


@router.post(
    path="/create",
    responses={
        status.HTTP_201_CREATED: {"model": dto.Customer}
    }
)
async def create_customer(
    customer_info: dto.CreateCustomer,
    service: Annotated[CreateCustomerService, Depends(Stub(CreateCustomerService))]
) -> dto.Customer:
    return await service(customer_info=customer_info)