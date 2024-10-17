"""Return User Profile."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, Header, Request, Response
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.redis_chash import cache_get_response
from src.core.controllers.depends.utils.return_error import http_exception
from src.core.controllers.depends.utils.serialize_user import serialize_user
from src.core.settings.const import CacheConf, MessageError
from src.core.validators import UserProfile

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


@cache_get_response(
    expire=CacheConf.CACHE_EXPIRATION_TIME_GET_USER,
    prefix_key=CacheConf.PREFIX_USER_ME,
)
async def get_me(
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
    request: Request,
    response: Response,
    if_none_match: str | None = Header(default=None),
) -> "UserProfile":
    """Return User's profile.

    Args:
        id_user: str: User ID retrieved from the access token.
        session: AsyncSession: Database session for querying user data.
        crud: Crud: Interface to perform database operations on user data.
        request: Request: HTTP request object from FastAPI.
        response: Response: HTTP response object to set headers.
        if_none_match: str | None: Optional ETag header for cache validation.

    Returns:
        pydantic.BaseModel: UserProfile: Serialized user's profile data.

    Notes:
        The profile is returned only if the request includes a valid token.
        Caching is applied to reduce database queries and enhance performance.
    """
    user_profile = await crud.users.get_me(
        id_user=id_user,
        session=session,
    )

    if not user_profile:
        # TODO LOGGER INFO {id} {request} {response} {if_none_match}
        print(request, response, if_none_match)
        http_exception(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            error_message=MessageError.MESSAGE_SERVER_ERROR,
            error_type=MessageError.TYPE_ERROR_500,
        )

    return UserProfile(result=True, user=serialize_user(user_profile))
