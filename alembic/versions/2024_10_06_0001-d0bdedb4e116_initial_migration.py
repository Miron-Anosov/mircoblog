"""Initial migration.

Revision ID: d0bdedb4e116
Revises:
Create Date: 2024-10-06 00:01:30.513898

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d0bdedb4e116"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  # noqa D103
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "followers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("follower_id", sa.UUID(), nullable=False),
        sa.Column("followed_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["followed_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tweets",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("author", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users_auth",
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column(
            "created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "likes",
        sa.Column("like_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("tweet_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tweet_id"],
            ["tweets.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("like_id"),
    )
    op.create_table(
        "media",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("source", sa.String(), nullable=False),
        sa.Column("tweet_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tweet_id"],
            ["tweets.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("source"),
    )
    op.create_table(
        "users_auth_ip",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("refresh_token", sa.String(), nullable=False),
        sa.Column("fingerprint", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users_auth.user_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:  # noqa D103
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_auth_ip")
    op.drop_table("media")
    op.drop_table("likes")
    op.drop_table("users_auth")
    op.drop_table("tweets")
    op.drop_table("followers")
    op.drop_table("users")
    # ### end Alembic commands ###
