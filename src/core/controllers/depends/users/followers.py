"""Dependency followers.

POST/DELETE:
/api/users/{id}/follow

"""

from typing import TYPE_CHECKING, Annotated, Optional

from fastapi import Depends

from src.core.controllers.depends.auth.check_token import (
    get_user_id_by_token_access,
)
from src.core.controllers.depends.utils.connect_db import get_crud, get_session
from src.core.controllers.depends.utils.return_error import raise_http_db_fail

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.core.models_orm.crud import Crud


async def post_follow(
    followed_id: Annotated[str, Depends(get_user_id_by_token_access)],
    user_id: str,
    session: Annotated["AsyncSession", Depends(get_session)],
    crud: Annotated["Crud", Depends(get_crud)],
) -> bool:
    """
    Create new follower.

    Args:
        followed_id (str): owner's ID.
        user_id (str): target user's ID.
        session (AsyncSession): async connection to db.
        crud (Crud): crud-worker's interface.
    Returns:
        bool: True if successful or raise HTTPException.
    Raises:
        HTTPException: if db return None.
    """
    is_follow: Optional[bool] = await crud.users.post_user_follow(
        followed_id=followed_id, follower_id=user_id, session=session
    )
    raise_http_db_fail(is_follow)

    return True
