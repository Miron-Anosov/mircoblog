"""Users CRUD methods."""

import abc
import uuid

from sqlalchemy import bindparam, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models_orm.crud_models.utils.catcher_errors import cather_sql_err
from src.core.models_orm.models.auth import UsersAuthORM
from src.core.models_orm.models.user_orm import UserORM


class _AuthInterface(abc.ABC):
    """Interface for auth-related operations."""

    @classmethod
    @abc.abstractmethod
    async def login_user(
        cls,
        email: str,
        session: AsyncSession,
        auth_user: UsersAuthORM,
    ) -> tuple:
        """Login exist user.

        Returns:
          str: user pwd if user exists, None otherwise.
        """
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
        table_auth: UsersAuthORM,
        table_user: UserORM,
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
    @cather_sql_err
    async def post_new_user(
        session: AsyncSession,
        auth_user: dict,
        table_auth: UsersAuthORM = UsersAuthORM,
        table_user: UserORM = UsersAuthORM,
    ) -> bool:
        """Create new user at DB.

        Create new user at auth_users.
        Create new user at users.

        Returns:
            bool
        """
        new_uuid = uuid.uuid4().hex
        auth_user["user_id"] = new_uuid

        await session.execute(
            insert(UserORM),
            params=[{"id": new_uuid, "name": auth_user["name"]}],
        )
        await session.execute(insert(UsersAuthORM), params=[auth_user])
        print("СОЗДАЮ НОВОГО ПОЛЬЗОВАТЕЛЯ")  # TODO: Add logger INFO
        await session.commit()

        return True

    @staticmethod
    @cather_sql_err
    async def if_exist_email(
        email: str,
        session: AsyncSession,
        table=UsersAuthORM,
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

    @classmethod
    @cather_sql_err
    async def login_user(
        cls,
        email: str,
        session: AsyncSession,
        auth_user=UsersAuthORM,
    ) -> tuple:
        """Login exist user.

        Returns:
          str: user pwd if user exists, None otherwise.
        """
        if _ := await cls.if_exist_email(email=email, session=session):
            user: UsersAuthORM = await session.scalar(
                statement=(
                    select(auth_user).where(
                        auth_user.email == bindparam("email")
                    )
                ),
                params=[{"email": email}],
            )
            return user.hashed_password, user.user_id

        return None, None

    @staticmethod
    async def logout_user(
        session: AsyncSession,
        user_id: dict,
    ) -> bool:
        """Logout."""
        return True  # TODO: Implement logic
