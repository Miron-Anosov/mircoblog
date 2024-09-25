"""Users CRUD methods."""

import abc

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models_orm.models.auth import UsersAuthORM


class _AuthInterface(abc.ABC):
    """Interface for auth-related operations."""

    @staticmethod
    @abc.abstractmethod
    async def login_user(
        email: str | None,
        username: str | None,
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
    async def check_if_exist_user(
        email: str | None,
        username: str | None,
        session: "AsyncSession",
        table: "UsersAuthORM",
    ) -> bool:
        """Check user in DB.

        new_user: UsersRoutes
        session: AsyncSession
        Return:
            - True: if user is already exists .
            - False: if user is not exist.
        """


class AuthUsers(_AuthInterface):
    """User crud interface."""

    @staticmethod
    async def post_new_user(
        session: AsyncSession,
        new_user: dict,
    ) -> bool:
        """Create new user."""
        print(new_user)
        # new_person = UsersAuthORM()
        # print(new_person)
        try:
            print(type(session))
            print(dir(session))
            await session.begin()
            print("СОЗДАЮ НОВОГО ПОЛЬЗОВАТЕЯ")  # TODO: Add logger INFO
            # session.add(new_person)
        except SQLAlchemyError:
            # todo: loger WARNING
            return False
        else:
            # todo: send email to new user
            return True

    @staticmethod
    async def check_if_exist_user(email, username, session, table) -> bool:
        """Check user in DB.

        new_user: UsersRoutes
        session: AsyncSession
        Return:
            - True: if user is already exists .
            - False: if user is not exist.
        """
        return True  # TODO: miss to make logic

    @staticmethod
    async def login_user(
        email: str | None,
        username: str | None,
        session: AsyncSession,
    ) -> bool:
        """Login."""
        return True  # TODO: miss to make logic

    @staticmethod
    async def logout_user(session: AsyncSession, user_id: dict) -> bool:
        """Logout."""
        return True  # TODO: miss to make logic
