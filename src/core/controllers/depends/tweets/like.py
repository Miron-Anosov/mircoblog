"""Create/Delete like for tweets.

/api/tweets/{id}/like
"""

from typing import TYPE_CHECKING, Annotated, Optional

from fastapi import Depends, status

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.return_error import http_exception
from src.core.settings.const import MessageError

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def post_like(
    tweet_id: str,
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> bool:
    """Create like for some tweets."""
    like_result = await crud.tweets.post_like(
        session=session, id_user=id_user, id_tweet=tweet_id
    )

    raise_http(is_none_result=like_result)

    return True


async def delete_like(
    tweet_id: str,
    id_user: Annotated[str, Depends(get_user_id_by_token_access)],
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> bool:
    """Create like for some tweets."""
    like_result = await crud.tweets.delete_like(
        session=session, id_user=id_user, id_tweet=tweet_id
    )

    raise_http(is_none_result=like_result)

    return True


def raise_http(is_none_result: Optional[bool]) -> None:
    """Checker None.

    Args:
        - is_none_result (Optional[bool]): result db.
    Raise:
        - HTTPException
    Nones:
        - If db finish incorrect a process than it'll return None.
    """
    if is_none_result is None:
        # todo: add logger info fail get tweets data from db
        raise http_exception(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type=MessageError.TYPE_ERROR_INTERNAL_SERVER_ERROR,
            error_message=MessageError.MESSAGE_SERVER_ERROR,
        )
