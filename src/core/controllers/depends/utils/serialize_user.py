"""Return UserMe model."""

from src.core.validators import User, UserMe


def serialize_user(user) -> "UserMe":
    """
    Serialize a user object into a Pydantic model 'UserMe'.

    Args:
        user: The user object containing information about
        followers and following.

    Returns:
        A 'UserMe' Pydantic model containing:
            - id: The user's ID as a string.
            - name: The user's name.
            - followers: A list of 'User' models representing followers, with
                their IDs and names.
            - following: A list of 'User' models representing users this user
                is following, with their IDs and names.

    Example:
        serialized_user = serialize_user(current_user)
    """
    return UserMe(
        id=str(user.id),
        name=user.name,
        followers=[
            User(id=str(follower.followed_id), name=follower.follower.name)
            for follower in user.followers
            if follower
        ],
        following=[
            User(id=str(followed.follower_id), name=followed.following.name)
            for followed in user.following
            if followed
        ],
    )
