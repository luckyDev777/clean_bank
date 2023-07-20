from src.adapters.db import models
from src.core.customer import dto_customer
from src.core.account import dto_account


def convert_customer_models_to_dto(customer: models.Customer) -> dto_customer.Customer:
    return dto_customer.Customer(
        customer_id=customer.id,
        name=customer.name,
        email=customer.email,
        phone_number=customer.phone_number,
        # accounts=customer.accounts
    )


def convert_account_model_to_dto(account: models.Account) -> dto_account.Account:
    return dto_account.Account(
        account_id=account.id,
        account_number=account.account_number,
        balance=account.balance,
        customer_id=account.customer_id,
    )
