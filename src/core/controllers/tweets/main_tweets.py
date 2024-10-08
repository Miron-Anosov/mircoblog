"""Tweets for micro_blog.

Routes:
    - del_like_tweet_by_id()
    - del_tweet_by_id()
    - get_tweets()
    - post_like_by_id()
    - post_new_tweet()
"""

import http
from typing import Sequence

from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer

from src.core.controllers.depends.auth.check_token import token_is_alive
from src.core.controllers.tweets.del_like import del_like
from src.core.controllers.tweets.del_tweet import del_tweet_by_id
from src.core.controllers.tweets.get_tweets import get_tweets
from src.core.controllers.tweets.post_like import post_like_by_id
from src.core.controllers.tweets.post_new_tweet import post_new_tweet
from src.core.settings.routes_path import TweetsRoutes
from src.core.validators import GetAllTweets, ReturnNewTweet, StatusResponse


def create_tweets_route() -> APIRouter:
    """Create tweets' routes.

    Return:
        - APIRouter
    Raises:
        - None
    Notes:
        - prefix: /api
        - tags: Tweets
    """
    return APIRouter(
        tags=[TweetsRoutes.TAG],
    )


tweets: APIRouter = create_tweets_route()

common_depends: Sequence[Depends] = [
    Depends(token_is_alive),
    Depends(HTTPBearer(auto_error=False)),
]

tweets.add_api_route(
    endpoint=post_new_tweet,
    methods=[http.HTTPMethod.POST],
    status_code=status.HTTP_201_CREATED,
    path=TweetsRoutes.TWEETS,
    response_model=ReturnNewTweet,
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=del_tweet_by_id,
    methods=[http.HTTPMethod.DELETE],
    status_code=status.HTTP_200_OK,
    path=TweetsRoutes.TWEETS_DEL_BY_ID,
    response_model=StatusResponse,
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=post_like_by_id,
    methods=[http.HTTPMethod.POST],
    status_code=status.HTTP_201_CREATED,
    path=TweetsRoutes.TWEETS_POST_DEL_ID_LIKE,
    response_model=StatusResponse,
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=get_tweets,
    methods=[http.HTTPMethod.GET],
    status_code=status.HTTP_200_OK,
    path=TweetsRoutes.TWEETS,
    response_model=GetAllTweets,
)

tweets.add_api_route(
    endpoint=del_like,
    methods=[http.HTTPMethod.DELETE],
    status_code=status.HTTP_200_OK,
    path=TweetsRoutes.TWEETS_POST_DEL_ID_LIKE,
    response_model=StatusResponse,
    dependencies=common_depends,
)
