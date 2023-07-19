from fastapi import FastAPI

from .customer import router as customer_router
from .exceptions import setup_exception_handlers
from .root import router as root_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(router=root_router)
    app.include_router(router=customer_router)

    setup_exception_handlers(app=app)
