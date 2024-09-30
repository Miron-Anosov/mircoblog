"""TODO DOCS."""

import datetime

import jwt

from src.core.settings.settings import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.jwt_tokens.private_token.read_text(),
    algorithm: str = settings.jwt_tokens.algorithm,
    expire_minutes: int = settings.jwt_tokens.access_token_expire_minutes,
    expire_delta: datetime.timedelta | None = None,
) -> str:
    """Return encoded token."""
    now = datetime.datetime.now(datetime.UTC)

    if expire_delta:
        expire = now + expire_delta
    else:
        expire = now + datetime.timedelta(minutes=expire_minutes)

    to_encode = payload.copy()
    to_encode["exp"] = expire
    to_encode["iat"] = now
    encode = jwt.encode(
        payload=to_encode,
        key=private_key,
        algorithm=algorithm,
    )
    return encode


def decode_jwt(
    jwt_token: str | bytes,
    public_key: str = settings.jwt_tokens.public_token.read_text(),
    algorithm: str = settings.jwt_tokens.algorithm,
) -> dict:
    """Return decoded token."""
    decoded = jwt.decode(
        jwt=jwt_token,
        key=public_key,
        algorithms=[algorithm],
    )
    return decoded
