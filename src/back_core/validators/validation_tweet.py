"""Validator models for /tweets.

You can see route to /src/back_core/controllers/tweets.py
"""

import uuid

import pydantic


class ValidPostModelNewTweetInput(pydantic.BaseModel):
    """**Model validate input date from route POST /tweets**.

    - `tweet_data`: str: Data post tweet.
    - `tweet_media_ids`: Pictures id with tweet.
    """

    tweet_data: str = pydantic.Field(description="Message to new post")
    tweet_media_ids: list[int] | None = pydantic.Field(
        strict=False, description="Array tweet IDs"
    )


class ValidPostModelNewTweetOutput(pydantic.BaseModel):
    """**Movel validate response POST /tweets**.

    - `result`: bool : Successful or unsuccessful.
    - `tweet_id`: UUID : Unique identifier for the tweet.
    """

    result: bool = pydantic.Field(
        description="Successful or unsuccessful",
    )
    tweet_id: uuid.UUID = pydantic.Field(
        default_factory=uuid.uuid4,
        description="Unique identifier for " "the tweet.",
    )


class ValidDeleteModelTweet(pydantic.BaseModel):
    """**Movel validate response DELETE /tweets**.

    - `result`: bool : Successful or unsuccessful.

    """

    result: bool = True
