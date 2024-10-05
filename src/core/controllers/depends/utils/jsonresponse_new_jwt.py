"""Return Response with tokens."""

from fastapi import status
from fastapi.responses import JSONResponse

from src.core.controllers.depends.utils.jwt_token import create_token
from src.core.settings.const import JWT
from src.core.validators import UserToken


def response(payload: dict) -> "JSONResponse":
    """Return JSONResponse with new tokens."""
    user_token = UserToken(
        access_token=create_token(
            payload=payload, type_token=JWT.TOKEN_TYPE_ACCESS
        ),
        refresh_token=create_token(
            payload=payload, type_token=JWT.TOKEN_TYPE_REFRESH
        ),
    )

    resp = JSONResponse(
        content=user_token.model_dump(
            exclude={
                JWT.TOKEN_TYPE_REFRESH,
                JWT.DESCRIPTION_PYDANTIC_EXPIRE_REFRESH,
            }
        ),
        status_code=status.HTTP_201_CREATED,
        media_type="application/json",
    )
    resp.set_cookie(
        key=JWT.TOKEN_TYPE_REFRESH,
        value=user_token.refresh_token,
        httponly=True,
        # secure=True,
        expires=user_token.expires_refresh,
    )
    return resp
