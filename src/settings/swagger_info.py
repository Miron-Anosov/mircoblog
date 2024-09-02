"""Description info for http://localhost:8000/docs/ ."""

from pathlib import Path

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
        "description": "Попробуй это.",
    },
]

CONTACT = {
    "name": "Miron",
    "url": "https://gitlab.com/miron.nicolaevich/",
    "email": "miron-nicolaevich@gmail.com",
}

SERVERS = [{"url": "http://127.0.0.1:8000"}]

__all__ = ["SUMMARY", "DESCRIPTION", "TAGS_METADATA", "CONTACT", "SERVERS"]
