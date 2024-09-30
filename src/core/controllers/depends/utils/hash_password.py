"""Hash user password."""

import bcrypt


def hash_pwd(
    password: str,
) -> bytes:
    """Create crypt hash password."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password=password.encode("UTF-8"), salt=salt)


def validate_pwd(password: str, hash_password: bytes) -> bool:
    """Validate crypt hash password."""
    return bcrypt.checkpw(
        password=password.encode("UTF-8"),
        hashed_password=hash_password,
    )
