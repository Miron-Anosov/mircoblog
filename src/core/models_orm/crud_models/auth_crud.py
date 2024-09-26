"""Users CRUD methods."""

import abc

from sqlalchemy import bindparam, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models_orm.models.auth import UsersAuthORM


class _AuthInterface(abc.ABC):
    """Interface for auth-related operations."""

    @staticmethod
    @abc.abstractmethod
    async def login_user(
        email: str,
        session: AsyncSession,
    ) -> bool:
        """Login."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def logout_user(session: AsyncSession, user_id: dict) -> bool:
        """Logout."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def post_new_user(
        session: AsyncSession,
        new_user: dict,
    ) -> bool:
        """Create new user."""

    @staticmethod
    @abc.abstractmethod
    async def if_exist_email(
        email: str,
        session: "AsyncSession",
        table: UsersAuthORM,
    ) -> bool:
        """Check user in DB.

        email: Users email
        session: AsyncSession
        Return:
            - True: if user is already exists.
            - False: if user is not exist.
        """


class AuthUsers(_AuthInterface):
    """User CRUD interface."""

    @staticmethod
    async def post_new_user(
        session: AsyncSession,
        new_user: dict,
    ) -> bool:
        """Create new user."""
        print(new_user)
        try:
            print(type(session))
            print(dir(session))
            await session.begin()
            print("СОЗДАЮ НОВОГО ПОЛЬЗОВАТЕЛЯ")  # TODO: Add logger INFO
        except SQLAlchemyError:
            # TODO: Logger WARNING
            return False
        else:
            # TODO: Send email to new user
            return True

    @staticmethod
    async def if_exist_email(
        email: str, session: AsyncSession, table=UsersAuthORM
    ) -> bool:
        """Check user in DB.

        email: Users email
        session: AsyncSession
        Return:
            - True: if user is already exists.
            - False: if user is not exist.
        """
        stmt = select(table.email).where(table.email == bindparam(key="email"))
        email_exist = await session.scalar(stmt, params={"email": email})
        return True if email_exist else False

    @staticmethod
    async def login_user(
        email: str,
        session: AsyncSession,
    ) -> bool:
        """Login."""
        return True  # TODO: Implement logic

    @staticmethod
    async def logout_user(
        session: AsyncSession,
        user_id: dict,
    ) -> bool:
        """Logout."""
        return True  # TODO: Implement logic
