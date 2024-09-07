"""Tweets for micro_blog."""

import http

from fastapi import APIRouter, Depends, status

from back_core.settings.routes_path import TweetsRoutes
from back_core.validators.valid_tweet import (
    ValidGETModelTweet,
    ValidPostModelNewTweetOutput,
    ValidStatusResponse,
)

from ..controller_dependends.http_handler_api_key import api_key_depend
from .del_like_tweet import del_like_tweet_by_id
from .del_tweet import del_tweet_by_id
from .get_tweets import get_tweets
from .post_like_tweet import post_like_by_id
from .post_new_tweet import post_new_tweet

tweets = APIRouter(
    tags=[TweetsRoutes.TAG.value],
    prefix=TweetsRoutes.PREFIX.value,
)


common_depends = [Depends(api_key_depend)]

tweets.add_api_route(
    endpoint=post_new_tweet,
    methods=[http.HTTPMethod.POST],
    status_code=status.HTTP_201_CREATED,
    path=TweetsRoutes.TWEETS.value,
    response_model=ValidPostModelNewTweetOutput,
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=del_tweet_by_id,
    methods=[http.HTTPMethod.DELETE],
    status_code=status.HTTP_200_OK,
    path=TweetsRoutes.TWEETS_POST_DEL_ID_LIKE.value,
    response_model=ValidStatusResponse,
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=post_like_by_id,
    methods=[http.HTTPMethod.POST],
    status_code=status.HTTP_201_CREATED,
    path=TweetsRoutes.TWEETS_POST_DEL_ID_LIKE.value,
    response_model=ValidStatusResponse,
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=get_tweets,
    methods=[http.HTTPMethod.GET],
    status_code=status.HTTP_200_OK,
    path=TweetsRoutes.TWEETS.value,
    response_model=ValidGETModelTweet,
    dependencies=common_depends,
)

tweets.add_api_route(
    endpoint=del_like_tweet_by_id,
    methods=[http.HTTPMethod.DELETE],
    status_code=status.HTTP_200_OK,
    path=TweetsRoutes.TWEETS.value,
    response_model=ValidGETModelTweet,
    dependencies=[Depends(api_key_depend)],
)
