"""SQLAlchemy LikesORM model."""

from typing import TYPE_CHECKING

from sqlalchemy import BIGINT, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from core.models_orm.models.tweet_orm import TweetsORM
    from core.models_orm.models.user_orm import UserORM


class LikesORM(BaseModel):
    """Likes ORM model.

    Table: likes
    """

    __tablename__ = "likes"
    __mapper_args__ = {"eager_defaults": True}
    like_id: Mapped[int] = mapped_column(
        BIGINT, primary_key=True, autoincrement=True
    )
    tweet_id: Mapped[UUID] = mapped_column(ForeignKey("tweets.id"))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    tweet: Mapped["TweetsORM"] = relationship(
        "TweetsORM",
        back_populates="likes",
    )
    user: Mapped["UserORM"] = relationship(
        "UserORM",
        back_populates="likes",
    )
