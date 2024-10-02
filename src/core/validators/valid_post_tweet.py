"""Validator models for POST /tweets.

You can see route to /src/back_core/controllers/tweets.py
"""

import uuid

import pydantic

from src.core.settings.const import PydanticTweets


class ValidPostModelNewTweetInput(pydantic.BaseModel):
    """**Model validate input date from route POST /tweets**.

    - `tweet_data`: str: Data post tweet.
    - `tweet_media_ids`: Pictures id with tweet.
    """

    tweet_data: str = pydantic.Field(
        description=PydanticTweets.TWEET_DATA_DESCRIPTION,
        min_length=PydanticTweets.TWEET_DATA_MIN_LENGTH_DESCRIPTION,
    )
    tweet_media_ids: list[int] | None = pydantic.Field(
        default=None,
        strict=False,
        description=PydanticTweets.TWEET_MEDIA_IDS_DESCRIPTION,
    )
    model_config = pydantic.ConfigDict(
        title=PydanticTweets.TITLE_TWEET_REQUEST
    )


class ValidPostModelNewTweetOutput(pydantic.BaseModel):
    """**Model validate response POST /tweets**.

    - `result`: bool : Successful or unsuccessful.
    - `tweet_id`: UUID : Unique identifier for the tweet.
    """

    result: bool = pydantic.Field(
        description=PydanticTweets.TWEET_RESULT_BOOL_DESCRIPTION, default=True
    )
    tweet_id: uuid.UUID = pydantic.Field(
        default_factory=uuid.uuid4,
        description=PydanticTweets.ID_DESCRIPTION,
    )

    model_config = pydantic.ConfigDict(
        title=PydanticTweets.TITLE_TWEETS_RESPONSE
    )
