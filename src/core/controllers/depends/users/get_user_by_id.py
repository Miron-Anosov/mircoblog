"""Return User Profile by ID."""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.serialize_user import serialize_user
from src.core.validators import UserProfile

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud

from fastapi import Header, Request, Response, status

from src.core.controllers.depends.utils.redis_chash import cache_get_response
from src.core.controllers.depends.utils.return_error import http_exception
from src.core.settings.const import CacheConf, MessageError


@cache_get_response(
    expire=CacheConf.CACHE_EXPIRATION_TIME_GET_USER,
    prefix_key=CacheConf.PREFIX_USER_BY_ID,
)
async def get_user_by_id(
    id: str,  # noqa
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
    request: Request,
    response: Response,
    if_none_match: str | None = Header(default=None),
) -> "UserProfile":
    """Return User's profile.

    Args:
        - id_user (str): user ID.
        - session (AsyncSession): db session.
        - crud (Crud): crud worker interface
    Returns:
        - UserProfile (pydantic model)
    Notes:
        - Return profile without a token.
    """
    user_profile = await crud.users.get_me(
        id_user=id,
        session=session,
    )

    if not user_profile:
        # TODO LOGGER INFO {id} {request} {response} {if_none_match}
        print(request, response, if_none_match)
        http_exception(
            status_code=status.HTTP_404_NOT_FOUND,
            error_message=MessageError.MESSAGE_SERVER_ERROR,
            error_type=MessageError.TYPE_ERROR_404,
        )

    return UserProfile(result=True, user=serialize_user(user_profile))
