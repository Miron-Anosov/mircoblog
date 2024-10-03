"""Users CRUD methods."""

from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.core.models_orm.crud_models.utils.catcher_errors import cather_sql_err
from src.core.models_orm.models.user_orm import UserORM


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
    async def get_me(
        id_user: str, session: AsyncSession, user_table=UserORM
    ) -> "UserORM":
        """Get current user info."""
        pass

    @staticmethod
    @abstractmethod
    async def get_user(
        id_user: str, session: AsyncSession, user_table: UserORM
    ) -> UserORM:
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
    async def get_me(
        id_user: str, session: AsyncSession, user_table=UserORM
    ) -> Optional["UserORM"]:
        """Get user by id."""
        query = (
            select(user_table)
            .options(
                selectinload(user_table.followers),
                selectinload(user_table.following),
            )
            .where(user_table.id == id_user)
        )
        return await session.scalar(query)

    @staticmethod
    @cather_sql_err
    async def get_user(
        id_user: str, session: AsyncSession, user_table=UserORM
    ) -> Optional["UserORM"]:
        """Get user by id."""
        query = (
            select(user_table)
            .options(
                selectinload(user_table.followers),
                selectinload(user_table.following),
            )
            .where(user_table.id == id_user)
        )
        return await session.scalar(query)
