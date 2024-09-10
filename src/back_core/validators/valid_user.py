"""Validator models for /tweets.

You can see route to /src/back_core/controllers/users.py
"""

import uuid

import pydantic


class ValidUserModel(pydantic.BaseModel):
    """**Model for tweet author details**.

     - `id`: str: Identification of user.
    - `name`: User's name.
    """

    id: uuid.UUID = pydantic.Field(
        default_factory=uuid.uuid4,
        description="Author's unique ID",
    )
    name: str = pydantic.Field(..., description="Author's name")

    model_config = pydantic.ConfigDict(title="User")


class ValidModelGetMe(pydantic.BaseModel):
    """Validate model for profile of user."""

    user: dict[str, ValidUserModel]
    followers: list[dict[str, ValidUserModel]]
    following: list[dict[str, ValidUserModel]]


class ValidateUserProfile(pydantic.BaseModel):
    """**Users' profile**.

    - `result`: bool : Successful or unsuccessful.
    - `user`: Dict of user objects containing the following fields:
        - `id`: int : Unique identifier of the user.
        - `name`: string : User's name.
        - `followers`: Dict of users.
            - `id`: int : Unique identifier of the user.
            - `name`: string : User's name.
        - `following`: Dict of users.
            - `id`: int : Unique identifier of the user.
            - `name`: string : User's name.
    """

    result: bool
    user: ValidModelGetMe

    class Config:
        """Config schema users' profile."""

        title = "User's profile"
        from_attributes = True
        json_schema_extra = {
            "example": {
                "result": True,
                "user": {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "Dick",
                    "followers": [
                        {
                            "id": "3fa33364-5717-4562-b3fc-2c963f66afa6",
                            "name": "Tom",
                        }
                    ],
                    "following": [
                        {
                            "id": "3fa33364-5717-4562-b3fc-2c963f4563fa6",
                            "name": "Ramil",
                        }
                    ],
                },
            }
        }
