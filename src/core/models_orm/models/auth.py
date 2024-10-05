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

    CREATE TABLE users_auth (
        user_id UUID NOT NULL,
        created TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
        hashed_password VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        PRIMARY KEY (user_id),
        UNIQUE (user_id),
        FOREIGN KEY(user_id) REFERENCES users (id),
        UNIQUE (email)
    )
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
