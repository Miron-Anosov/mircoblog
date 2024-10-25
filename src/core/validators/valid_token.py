"""Valid User token."""

import datetime

import pydantic

from src.core.settings.const import JWT
from src.core.settings.settings import settings


class ValidTokenInfo(pydantic.BaseModel):
    """User's uniq api-key.

    `access_token` uses for authorisation for users.
    `token_type`: Bearer
    """

    access_token: str = pydantic.Field(
        description=JWT.DESCRIPTION_PYDANTIC_ACCESS_TOKEN,
    )
    refresh_token: str = pydantic.Field(
        description=JWT.DESCRIPTION_PYDANTIC_REFRESH_TOKEN,
    )
    expires_refresh: datetime.datetime = pydantic.Field(
        default_factory=lambda: datetime.datetime.now(datetime.UTC)
        + datetime.timedelta(days=settings.jwt.refresh_token_expire_days)
    )
    token_type: str = JWT.DESCRIPTION_PYDANTIC_TOKEN_TYPE
    model_config = pydantic.ConfigDict(title=JWT.DESCRIPTION_PYDANTIC_TITLE)
