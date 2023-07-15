from src.adapters.db import models
from src.core.customer import dto


def convert_customer_models_to_dto(customer: models.Customer) -> dto.Customer:
    return dto.Customer(
        customer_id=customer.id,
        name=customer.name,
        email=customer.email,
        phone_number=customer.phone_number
    )