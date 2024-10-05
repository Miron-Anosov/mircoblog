"""Create/Delete like for tweets.

/api/tweets/{id}/like
"""

from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.return_error import raise_http_db_fail

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

    raise_http_db_fail(is_none_result=like_result)

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

    raise_http_db_fail(is_none_result=like_result)

    return True
