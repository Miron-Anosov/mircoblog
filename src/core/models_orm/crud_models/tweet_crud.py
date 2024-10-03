"""Tweets CRUD methods."""

import abc
import uuid
from typing import Any, Sequence

from sqlalchemy import Row, RowMapping, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.core.models_orm.crud_models.utils.catcher_errors import cather_sql_err
from src.core.models_orm.models.tweet_orm import TweetsORM


class _TweetInterface(abc.ABC):
    """Interface for tweet-related operations."""

    @staticmethod
    @abc.abstractmethod
    async def post_like(
        session: AsyncSession, id_tweet: int, model: "TweetsORM"
    ) -> None:
        """Create like for tweet by id tweet."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def delete_like(
        session: AsyncSession, id_tweet: int, model: "TweetsORM"
    ) -> bool:
        """Delete like for tweet by id tweet."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def post_tweet(
        session: AsyncSession,
        user_id: int,
        content_test: str,
        content_media_ids: list[int],
        table=TweetsORM,
    ) -> str:
        """Create new tweet."""
        pass

    @staticmethod
    @abc.abstractmethod
    async def delete_tweet(
        session: AsyncSession,
        id_tweet: int,
    ) -> bool:
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
    @cather_sql_err
    async def post_like(session, id_tweet, model) -> None:
        """Create like for tweet by id tweet."""
        _ = await session.get(id_tweet, model)
        # TODO: miss to make logic

    @staticmethod
    async def delete_like(session, id_tweet, model) -> bool:
        """Delete like for tweet by id tweet."""
        _ = await session.get(id_tweet, model)
        return True  # TODO: miss to make logic

    @staticmethod
    @cather_sql_err
    async def post_tweet(
        session: AsyncSession,
        user_id: str,
        content_test: str,
        content_media_ids: list[int],
        table=TweetsORM,
    ) -> str | None:
        """Create new tweet."""
        new_tweet = table(
            id=uuid.uuid4().hex, content=content_test, author=user_id
        )
        con = await session.begin()
        session.add(new_tweet)
        await con.commit()

        return new_tweet.id

    @staticmethod
    @cather_sql_err
    async def delete_tweet(
        session: AsyncSession,
        id_tweet: int,
    ) -> bool:
        """Delete tweet by id."""
        print("delete tweet")
        return True  # TODO: miss to make logic

    @staticmethod
    @cather_sql_err
    async def get_tweets(
        session: AsyncSession, model_tweets: TweetsORM = TweetsORM
    ) -> Sequence[Row[Any] | RowMapping | Any] | None:
        """Create like for tweet by id tweet."""
        query = select(model_tweets).options(
            selectinload(model_tweets.likes),
            selectinload(model_tweets.attachments),
            selectinload(model_tweets.owner),
        )
        tweets = await session.scalars(query)
        return tweets.all()
