"""Return tweets."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.connect_db import get_crud, get_session
from src.core.validators import GetAllTweets

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def get_tweets_data(
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> "GetAllTweets":
    """Return tweets."""
    tweets = await crud.tweets.get_tweets(session=session)
    return GetAllTweets(tweets=tweets)
