"""Description info for http://localhost:8000/docs/ ."""

from pathlib import Path

from .settings import settings

SUMMARY = (
    "This API working with MicroBlog data."
    "Functional ability:\
    - User can add new post.\
    - User can delete him post.\
    - User can follow another users.\
    - User can unfollow another users.\
    - User can mark post.\
    - User can unmark post.\
    - User can receive news from posts in descending\
                                 order of popularity from users they follow.\
    - A post can include a picture."
)
_file_description_path = Path(__file__).parent / "description.md"
DESCRIPTION = Path(_file_description_path).read_text()

TAGS_METADATA = [
    {
        "name": "Methods API",
        "description": "Try use this.",
    },
]

CONTACT = {
    "name": settings.prod.CONTACT_NAME,
    "url": settings.prod.CONTACT_URL,
    "email": settings.prod.CONTACT_EMAIL,
}

SERVERS = [{"url": "http://localhost:8000"}]

VERSION_API = settings.prod.VERSION_API

TITLE = "MicroBlog API"

__all__ = [
    "SUMMARY",
    "DESCRIPTION",
    "TAGS_METADATA",
    "CONTACT",
    "SERVERS",
    "VERSION_API",
    "TITLE",
]
