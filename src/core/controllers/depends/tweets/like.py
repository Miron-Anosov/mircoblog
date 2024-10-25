"""Create/Delete like for tweets.

/api/tweets/{id}/like
"""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends, status

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.return_error import (
    raise_http_404,
    raise_http_500_if_none,
    valid_id_or_error_422,
)
from src.core.settings.const import MessageError

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def post_like(
    id: str,  # noqa
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> bool:
    """Create like for some tweets."""
    valid_id_or_error_422(request_id=id)

    like_result = await crud.tweets.post_like(
        session=session, id_user=id_user, id_tweet=id
    )
    raise_http_500_if_none(is_none_result=like_result)

    return (
        True
        if like_result
        else raise_http_404(
            status_code=status.HTTP_404_NOT_FOUND,
            error_type=MessageError.INVALID_ID_ERR,
            error_message=MessageError.INVALID_ID_ERR_MESSAGE_404,
        )
    )


async def delete_like(
    id: str,  # noqa
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> bool:
    """Create like for some tweets."""
    valid_id_or_error_422(request_id=id)

    like_result = await crud.tweets.delete_like(
        session=session, id_user=id_user, id_tweet=id
    )

    raise_http_500_if_none(is_none_result=like_result)

    return True
