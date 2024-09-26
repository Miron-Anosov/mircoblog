"""SQLAlchemy UserORM model."""

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.auth import UsersAuthORM
    from src.core.models_orm.models.tweet_orm import TweetsORM


class UserORM(BaseModel):
    """User ORM model.

    Table: users
    """

    __tablename__ = "users"
    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(nullable=False)

    followers: Mapped[list["UserORM"]] = relationship(
        "UserORM",
        secondary="followers",
        primaryjoin="UserORM.id==FollowersORM.following_id",
        secondaryjoin="UserORM.id==FollowersORM.follower_id",
        back_populates="following",
    )
    following: Mapped[list["UserORM"]] = relationship(
        "UserORM",
        secondary="followers",
        primaryjoin="UserORM.id==FollowersORM.follower_id",
        secondaryjoin="UserORM.id==FollowersORM.following_id",
        back_populates="followers",
    )

    users_profile: Mapped["UsersAuthORM"] = relationship(
        "UsersAuthORM", back_populates="user_auth"
    )
    users_likes: Mapped["TweetsORM"] = relationship(
        "TweetsORM", back_populates="likes"
    )
