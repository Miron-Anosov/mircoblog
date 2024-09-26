"""SQLAlchemy LikesORM model."""

from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from core.models_orm.models.user_orm import UserORM


class LikesORM(BaseModel):
    """Likes ORM model.

    Table: likes
    """

    __tablename__ = "likes"
    __mapper_args__ = {"eager_defaults": True}
    follower_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"), primary_key=True
    )
    following_id: Mapped[UUID] = mapped_column(
        ForeignKey("tweets.id"), primary_key=True
    )
