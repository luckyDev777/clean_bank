from functools import wraps
from typing import Callable, Any

from sqlalchemy.exc import SQLAlchemyError

from src.core.common.exceptions.dao import DAOError


def exception_mappper(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    async def wrapped(*args: Any, **kwargs: Any):
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError:
            raise DAOError
        
    return wrapped