"""Return UserMe model."""

from src.core.validators import User, UserMe


def serialize_user(user) -> "UserMe":
    """Return pydantic model UserProfile."""
    return UserMe(
        id=str(user.id),
        name=user.name,
        followers=[
            User(id=str(follower.id), name=follower.name)
            for follower in user.followers
        ],
        following=[
            User(id=str(followed.id), name=followed.name)
            for followed in user.following
        ],
    )
