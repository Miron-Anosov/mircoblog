"""Validator like models for /tweets.

You can see route to /src/back_core/controllers/
"""

import uuid

import pydantic


class ValidLikeModel(pydantic.BaseModel):
    """**Likes of tweet**."""

    user_id: uuid.UUID
    name: str = pydantic.Field(..., description="User's name")
    model_config = pydantic.ConfigDict(title="Like Tweet")
