"""Tweets CRUD methods."""

import abc
import uuid
from typing import Any, Sequence

from sqlalchemy import Row, RowMapping, Select, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.core.models_orm.crud_models.utils.catcher_errors import (
    catch_orm_critical_err,
)
from src.core.models_orm.models.likes_models import LikesORM
from src.core.models_orm.models.tweet_orm import TweetsORM


class _TweetInterface(abc.ABC):
    """Interface for tweet-related operations."""

    @staticmethod
    @abc.abstractmethod
    async def post_like(
        session: AsyncSession,
        id_tweet: str,
        id_user: str,
        like_table=LikesORM,
        model_like: LikesORM = LikesORM,
    ) -> None | bool:
        """Create like for tweet by id tweet."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def delete_like(
        session: AsyncSession,
        id_tweet: str,
        id_user: str,
        like_table=LikesORM,
    ) -> bool | None:
        """Delete like for tweet by id tweet."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def post_tweet(
        session: AsyncSession,
        user_id: str,
        content_test: str,
        content_media_ids: list[int],
        table=TweetsORM,
    ) -> str | None:
        """Create new tweet."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def delete_tweet(
        session: AsyncSession,
        id_tweet: str,
        id_user: str,
        table_tweet: "TweetsORM",
    ) -> bool | None:
        """Delete tweet by id."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def get_tweets(session: AsyncSession, model: "TweetsORM") -> None:
        """Create like for tweet by id tweet."""
        pass


class Tweets(_TweetInterface):
    """Tweets CRUD methods."""

    @staticmethod
    @catch_orm_critical_err
    async def post_like(
        session: AsyncSession,
        id_tweet: str,
        id_user: str,
        like_table=LikesORM,
    ) -> bool | None:
        """
        Create like for a tweet.

        Args:
            session (AsyncSession): Database session.
            id_tweet (str): Tweet ID.
            id_user (str): User ID.
            like_table (LikesORM()): Like model.

        Returns:
            bool | None: Success status.
        """
        like_exist = (
            select(like_table)
            .where(like_table.user_id == id_user)
            .where(like_table.tweet_id == id_tweet)
        )
        conn = await session.begin()

        if _ := await conn.session.scalar(like_exist) is not None:

            like_post = like_table(tweet_id=id_tweet, user_id=id_user)

            session.add(like_post)

            await conn.commit()

            return True

        return False

    @staticmethod
    @catch_orm_critical_err
    async def delete_like(
        session: AsyncSession,
        id_tweet: str,
        id_user: str,
        like_table=LikesORM,
    ) -> bool | None:
        """
        Delete like for a tweet.

        Args:
            session (AsyncSession): Database session.
            id_tweet (str): Tweet ID.
            id_user (str): User ID.
            like_table (LikesORM): Like model.

        Returns:
            bool | None: Success status.
        """
        stmt = (
            delete(like_table)
            .where(like_table.tweet_id == id_tweet)
            .where(like_table.user_id == id_user)
        )
        conn = await session.begin()
        await conn.session.execute(statement=stmt)
        await conn.commit()

        return True

    @staticmethod
    @catch_orm_critical_err
    async def post_tweet(
        session: AsyncSession,
        user_id: str,
        content_test: str,
        content_media_ids: list[int],
        table=TweetsORM,
    ) -> str | None:
        """
        Create new tweet.

        Args:
            session (AsyncSession): Database session.
            user_id (str): User ID.
            content_test (str): Tweet content.
            content_media_ids (list[int]): List of media IDs.
            table (TweetsORM()): Tweet model.

        Returns:
            str | None: New tweet ID.
        """
        new_tweet = table(
            id=uuid.uuid4().hex, content=content_test, author=user_id
        )
        con = await session.begin()
        session.add(new_tweet)
        await con.commit()

        return new_tweet.id

    @staticmethod
    @catch_orm_critical_err
    async def delete_tweet(
        session: AsyncSession,
        id_tweet: str,
        id_user: str,
        table_tweet=TweetsORM,
    ) -> bool | None:
        """
        Delete a tweet.

        Args:
            session (AsyncSession): Database session.
            id_tweet (str): Tweet ID.
            id_user (str): User ID.
            table_tweet (TweetsORM): Tweet model.

        Returns:
            bool | None: Success status.
        """
        stmt = (
            delete(table_tweet)
            .where(table_tweet.owner.has(id=id_user))
            .where(table_tweet.id == id_tweet)
        )
        con = await session.begin()
        await con.session.execute(statement=stmt)
        await con.commit()
        return True

    @staticmethod
    @catch_orm_critical_err
    async def get_tweets(
        session: AsyncSession,
        model_tweets: TweetsORM = TweetsORM,
        model_like: LikesORM = LikesORM,
    ) -> Sequence[Row[Any] | RowMapping | Any] | None:
        """
        Get all tweets.

        Args:
            session (AsyncSession): Database session.
            model_tweets (TweetsORM): Tweet model.
            model_like (LikesORM): Like model.

        Returns:
            Sequence[Row | RowMapping | Any] | None: List of tweets.
        """
        query: Select[Any] = select(model_tweets).options(
            selectinload(model_tweets.likes).selectinload(model_like.user),
            selectinload(model_tweets.attachments),
            selectinload(model_tweets.owner),
        )
        tweets = await session.scalars(query)
        return tweets.all()
