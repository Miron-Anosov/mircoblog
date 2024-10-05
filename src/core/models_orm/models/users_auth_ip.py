"""SQLAlchemy UsersAuthORM model."""

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
    user_id: Mapped[str] = mapped_column(
        UUID, primary_key=True, default=uuid.uuid4, unique=True
    )
    api_key: Mapped[str]
    created_key: Mapped[datetime] = mapped_column(nullable=False)
