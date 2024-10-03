"""Decorator for SQLAlchemyError."""

from collections.abc import Callable
from functools import wraps

from sqlalchemy.exc import SQLAlchemyError


def cather_sql_err(function: Callable) -> Callable:
    """Catch SQLAlchemyError and return None."""

    @wraps(function)
    def wrapper(*args, **kwargs) -> Callable | None:
        try:
            return function(*args, **kwargs)
        except SQLAlchemyError as e:
            print(str(e))
            # TODO add loger WARNING
            return None

    return wrapper
