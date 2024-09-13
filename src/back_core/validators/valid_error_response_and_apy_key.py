"""Error Response to clients."""

import pydantic


class ValidErrorResponse(pydantic.BaseModel):
    """Response error.

    If Api will have any errors, it will send to client.
    """

    result: bool
    error_type: str
    error_message: str

    model_config = pydantic.ConfigDict(title="Bad Request")


class ValidApiKey(pydantic.BaseModel):
    """User's uniq api-key.

    `apy-key` uses for authorisation for users.
    """

    api_key: str = pydantic.Field(
        default=None, description="String key.", min_length=6, max_length=60
    )

    model_config = pydantic.ConfigDict(title="api-key")
