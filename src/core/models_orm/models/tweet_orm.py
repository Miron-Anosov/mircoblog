"""SQLAlchemy TweetORM model."""

from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.media_orm import MediaORM
    from src.core.models_orm.models.user_orm import UserORM


class TweetsORM(BaseModel):
    """Tweets model."""

    __tablename__ = "tweets"
    id: Mapped[str] = mapped_column(UUID, primary_key=True)
    content: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(ForeignKey("users.id"))
    likes: Mapped[list["UserORM"]] = relationship(back_populates="users_likes")
    attachments: Mapped[list["MediaORM"]] = relationship(
        back_populates="tweets", cascade="all, delete-orphan"
    )
