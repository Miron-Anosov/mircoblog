"""SQLAlchemy MediaORM model."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models_orm.models.base_model import BaseModel

if TYPE_CHECKING:
    from src.core.models_orm.models.tweet_orm import TweetsORM


class MediaORM(BaseModel):
    """Media ORM model.

    Table: media

        CREATE TABLE media (
        id SERIAL NOT NULL,
        links VARCHAR NOT NULL,
        tweet_id UUID NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (links),
        FOREIGN KEY(tweet_id) REFERENCES tweets (id)
    )
    """

    __tablename__ = "media"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    links: Mapped[str] = mapped_column(unique=True)
    tweet_id: Mapped[str] = mapped_column(ForeignKey("tweets.id"))
    tweets: Mapped["TweetsORM"] = relationship(back_populates="attachments")
