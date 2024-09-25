"""Users CRUD methods."""

from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

# from src.back_core.models_orm.models.tweet_orm import (
#     UserORM as _User
# )


# from src.back_core.models_orm.models


class _UserInterface(ABC):
    """Interface for user-related operations."""

    @staticmethod
    @abstractmethod
    async def post_user_follow(id_user: int) -> None:
        """Follow user by id."""
        pass

    @staticmethod
    @abstractmethod
    async def delete_user_follow(session: AsyncSession, id_user: int) -> None:
        """Unfollow user by id."""
        pass

    @staticmethod
    @abstractmethod
    async def get_me() -> dict:
        """Get current user info."""
        pass

    @staticmethod
    @abstractmethod
    async def get_user(id_user: int) -> dict:
        """Get user by id."""
        pass

    @staticmethod
    @abstractmethod
    async def create_user(session: AsyncSession, new_user: dict) -> dict:
        """Get user by id."""
        pass


class Users(_UserInterface):
    """User crud interface."""

    @staticmethod
    async def post_user_follow(id_user) -> None:
        """Follow user by id."""
        pass

    @staticmethod
    async def delete_user_follow(session, id_user) -> None:
        """Unfollow user by id."""
        pass

    @staticmethod
    async def get_me() -> dict:
        """Get current user info."""
        return {}  # TODO: miss to make logic

    @staticmethod
    async def get_user(id_user: int) -> dict:
        """Get user by id."""
        return {}  # TODO: miss to make logic

    @staticmethod
    async def create_user(session, new_user) -> dict:
        """Get user by id."""
        return {}  # TODO: miss to make logic
