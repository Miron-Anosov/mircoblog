"""SQLAlchemy UsersAuthORM model."""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.auth import UsersAuthORM


class UsersAuthIPORM(BaseModel):
    """UsersAuthIPORM model.

        CREATE TABLE users_auth_ip (
        user_id UUID NOT NULL,
        api_key VARCHAR NOT NULL,
        created_key TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        PRIMARY KEY (user_id),
        UNIQUE (user_id)
    )
    """

    __tablename__ = "users_auth_ip"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(
        UUID,
        ForeignKey("users_auth.user_id"),
    )
    refresh_token: Mapped[str]
    fingerprint: Mapped[str] = mapped_column(nullable=False)
