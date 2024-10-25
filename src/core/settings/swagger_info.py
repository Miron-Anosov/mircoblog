"""Description info for http://localhost:8000/docs/ ."""

from pathlib import Path

from .settings import settings

SUMMARY = (
    "Добро пожаловать в MicroBlog API! Это интерфейс для работы с данными\
     микроблога, который позволяет вам легко управлять постами, медиафайлами\
      и подписками на пользователей. Надеемся, что API будет удобным и \
      полезным в вашей работе.\n\n"
    "Если у вас возникнут вопросы или потребуется помощь,\
     не стесняйтесь обращаться к нам по нижеуказанным контактам."
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
    "name": settings.open_api.CONTACT_NAME,
    "url": settings.open_api.CONTACT_URL,
    "email": settings.open_api.CONTACT_EMAIL,
}

SERVERS = [
    {"url": "http://localhost:8000"},
    {"url": "http://localhost:8001"},
]

VERSION_API = settings.open_api.VERSION_API

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
