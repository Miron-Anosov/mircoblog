"""Tweets CRUD methods."""

import abc
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
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
        session: AsyncSession, content: str, model: "TweetsORM"
    ) -> int:
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


class Tweets(_TweetInterface):
    """Tweets CRUD methods."""

    @staticmethod
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
    async def post_tweet(
        session,
        content: str,
        model,
    ) -> int:
        """Create new tweet."""
        return 1  # TODO: miss to make logic

    @staticmethod
    async def delete_tweet(
        session: AsyncSession,
        id_tweet: int,
    ) -> bool:
        """Delete tweet by id."""
        print("delete tweet")
        return True  # TODO: miss to make logic
