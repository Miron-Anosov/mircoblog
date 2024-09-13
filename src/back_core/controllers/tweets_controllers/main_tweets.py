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

from src.back_core.settings.routes_path import TweetsRoutes
from src.back_core.validators import (
    GetAllTweets,
    ReturnNewTweet,
    StatusResponse,
)

from ..controller_depends.http_handler_api_key import api_key_depend
from .del_like_tweet import del_like_tweet_by_id
from .del_tweet import del_tweet_by_id
from .get_tweets import get_tweets
from .post_like_tweet import post_like_by_id
from .post_new_tweet import post_new_tweet


def create_tweets_route() -> APIRouter:
    """Create tweets' routes.

    Return:
        APIRouter
    """
    return APIRouter(
        tags=[TweetsRoutes.TAG],
        prefix=TweetsRoutes.PREFIX,
    )


tweets: APIRouter = create_tweets_route()

common_depends: Sequence[Depends] = [Depends(api_key_depend)]

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
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=del_like_tweet_by_id,
    methods=[http.HTTPMethod.DELETE],
    status_code=status.HTTP_200_OK,
    path=TweetsRoutes.TWEETS_POST_DEL_ID_LIKE,
    response_model=StatusResponse,
    dependencies=[Depends(api_key_depend)],
)
