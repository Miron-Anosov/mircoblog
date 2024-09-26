"""SQLAlchemy UsersAuthORM model."""

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.user_orm import UserORM


class UsersAuthORM(BaseModel):
    """UsersAuthORM model.

    Table: users_auth
    user_id: str
    hashed_password: str
    email: str
    """

    __tablename__ = "users_auth"
    user_id: Mapped[str] = mapped_column(
        UUID,
        ForeignKey("users.id"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
    )
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    user_auth: Mapped["UserORM"] = relationship(back_populates="users_profile")
