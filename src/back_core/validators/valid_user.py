"""Validator models for /tweets.

You can see route to /src/back_core/controllers/users.py
"""

import uuid

import pydantic


class ValidUserModel(pydantic.BaseModel):
    """Model for tweet author details."""

    id: uuid.UUID = pydantic.Field(
        default_factory=uuid.uuid4,
        description="Author's unique ID",
    )
    name: str = pydantic.Field(..., description="Author's name")

    model_config = pydantic.ConfigDict(title="User")
