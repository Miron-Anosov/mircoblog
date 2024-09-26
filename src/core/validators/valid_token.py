"""Valid User token."""

import pydantic


class ValidTokenInfo(pydantic.BaseModel):
    """User's uniq api-key.

    `apy-key` uses for authorisation for users.
    """

    access_token: str = pydantic.Field(
        default=None, description="String key.", min_length=6, max_length=60
    )
    token_type: str
    model_config = pydantic.ConfigDict(title="Token")
