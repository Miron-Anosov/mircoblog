"""Valid User token."""

import pydantic


class ValidApiKey(pydantic.BaseModel):
    """User's uniq api-key.

    `apy-key` uses for authorisation for users.
    """

    api_key: str = pydantic.Field(
        default=None, description="String key.", min_length=6, max_length=60
    )

    model_config = pydantic.ConfigDict(title="api-key")
