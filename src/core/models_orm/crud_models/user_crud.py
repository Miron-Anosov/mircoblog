"""Users CRUD methods."""

from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from src.core.models_orm.crud_models.utils.catcher_errors import (
    catch_orm_critical_err,
)
from src.core.models_orm.models.followers_orm import FollowersORM
from src.core.models_orm.models.user_orm import UserORM


class _UserInterface(ABC):
    """Interface for user-related operations."""

    @staticmethod
    @abstractmethod
    async def post_user_follow(
        myself_id: str,
        user_id: str,
        session: "AsyncSession",
        follow_table=FollowersORM,
    ) -> bool | None:
        """Follow user by id."""
        pass

    @staticmethod
    @abstractmethod
    async def delete_user_follow(
        followed_id: str,
        follower_id: str,
        session: "AsyncSession",
        follow_table=FollowersORM,
    ) -> bool | None:
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
    """CRUD interface for user-related operations.

    This class provides methods to handle user-related actions, such as
    following/unfollowing users and retrieving user information.
    """

    @staticmethod
    # @catch_orm_err
    async def post_user_follow(
        followed_id: str,
        follower_id: str,
        session: "AsyncSession",
        follow_table=FollowersORM,
    ) -> bool | None:
        """Follow a user by ID.

        This method allows a user (follower) to follow another user
        (followed). If the user is already followed, the function returns
        `True` without adding a duplicate entry.

        Args:
            followed_id (str): The ID of the user being followed.
            follower_id (str): The ID of the user who is following.
            session (AsyncSession): The database session.
            follow_table (FollowersORM): The followers ORM table
                (defaults to `FollowersORM`).

        Returns:
            bool: Returns `True` if the follow operation was successful, or
            `None` in case of failure.
        """
        follow_exist = (
            select(follow_table)
            .where(follow_table.follower_id == follower_id)
            .where(follow_table.followed_id == followed_id)
        )

        follow = FollowersORM(follower_id=follower_id, followed_id=followed_id)

        conn = await session.begin()

        if _ := await conn.session.scalar(statement=follow_exist) is not None:
            return True
        try:
            conn.session.add(follow)
            await conn.commit()
            return True
        except IntegrityError:
            # TODO: ADD LOGER WARNING WITH exc
            return False

    @staticmethod
    @catch_orm_critical_err
    async def delete_user_follow(
        followed_id: str,
        follower_id: str,
        session: "AsyncSession",
        follow_table=FollowersORM,
    ) -> bool | None:
        """Unfollow a user by ID.

        This method allows a user (follower) to unfollow another user
        (followed).

        Args:
            followed_id (str): The ID of the user being unfollowed.
            follower_id (str): The ID of the user who is unfollowing.
            session (AsyncSession): The database session.
            follow_table (FollowersORM): The followers ORM table
                (defaults to `FollowersORM`).

        Returns:
            bool: Returns `True` if the unfollow operation was successful, or
            `None` in case of failure.
        """
        del_follow_stmt = (
            delete(follow_table)
            .where(follow_table.followed_id == followed_id)
            .where(follow_table.follower_id == follower_id)
        )
        connect = await session.begin()
        await connect.session.execute(del_follow_stmt)
        await connect.commit()
        return True

    @staticmethod
    @catch_orm_critical_err
    async def get_me(
        id_user: str, session: AsyncSession, user_table=UserORM
    ) -> Optional["UserORM"]:
        """Retrieve the current user information by ID.

        This method returns the details of the current user, including
        the followers and the users being followed.

        Args:
            id_user (str): The ID of the current user.
            session (AsyncSession): The database session.
            user_table (UserORM): The users ORM table (defaults to `UserORM`).

        Returns:
            Optional[UserORM]: Returns the user object if found, or `None`
            if no such user exists.
        """
        query = (
            select(user_table)
            .options(
                joinedload(user_table.followers).joinedload(
                    FollowersORM.follower
                ),
                joinedload(user_table.following).joinedload(
                    FollowersORM.following
                ),
            )
            .where(user_table.id == id_user)
        )
        return await session.scalar(query)

    @staticmethod
    @catch_orm_critical_err
    async def get_user(
        id_user: str, session: AsyncSession, user_table=UserORM
    ) -> Optional["UserORM"]:
        """Retrieve a user by ID.

        This method returns the details of the specified user, including
        their followers and the users they are following.

        Args:
            id_user (str): The ID of the user to retrieve.
            session (AsyncSession): The database session.
            user_table (UserORM): The users ORM table (defaults to `UserORM`).

        Returns:
            Optional[UserORM]: Returns the user object if found, or `None`
            if no such user exists.
        """
        query = (
            select(user_table)
            .options(
                selectinload(user_table.followers),
                selectinload(user_table.following),
            )
            .where(user_table.id == id_user)
        )
        return await session.scalar(query)
