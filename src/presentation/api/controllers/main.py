from fastapi import FastAPI

from .customer import router as customer_router
from .account import router as account_router
from .exceptions import setup_exception_handlers
from .root import router as root_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(router=root_router)
    app.include_router(router=customer_router)
    app.include_router(router=account_router)

    setup_exception_handlers(app=app)
