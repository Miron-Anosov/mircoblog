"""Main FastAPI module.

It here will be documentation about major information of API.

Functional ability:
    - User can add new post.
    - User can delete post.
    - User can follow another users.
    - User can unfollow another users.
    - User can mark post.
    - User can unmark post.
    - User can receive news from posts in descending
                                 order of popularity from users they follow.
    - A post can include a picture.

"""

import uvicorn
from fastapi import FastAPI

from back_core.controllers.media import media
from back_core.controllers.tweets import tweets
from settings import swagger_info


def create_app() -> FastAPI:
    """Maker FastAPI."""
    app_ = FastAPI(
        title=swagger_info.TITLE,
        description=swagger_info.DESCRIPTION,
        version=swagger_info.VERSION_API,
        openapi_tags=swagger_info.TAGS_METADATA,
        contact=swagger_info.CONTACT,
        servers=swagger_info.SERVERS,
        summary=swagger_info.SUMMARY,
        prefix="/api",
    )

    app_.include_router(router=media)
    app_.include_router(router=tweets)
    return app_


if __name__ == "__main__":
    app: FastAPI = create_app()
    uvicorn.run(
        create_app,
        host="0.0.0.0",
        port=8001,
        log_level="info",
        factory=True,
        # uds='./web_socks_backend'
    )
