"""Test valid get tweets."""

import uuid
from typing import Any, Dict, List, cast

import pytest
from pydantic import ValidationError

from src.back_core.validators.valid_get_tweets import ValidGETModelTweet
from tests.common_data import tweets_data


def test_get_models_tweet() -> None:
    """Test ValidGETModelTweet."""
    assert ValidGETModelTweet(**tweets_data)
    tweets = ValidGETModelTweet(**tweets_data)

    assert tweets.result is True
    assert len(tweets.tweets) == 1

    tweet = tweets.tweets[0]
    assert isinstance(tweet.id, uuid.UUID)
    assert tweet.content == "This is a sample tweet"
    if attachment := tweet.attachments:
        assert len(attachment) == 2
    assert tweet.author.name == "Author Name"
    assert len(tweet.likes) == 1
    assert tweet.likes[0].name == "User1"


def test_invalid_get_models_tweet() -> None:
    """Test ValidGETModelTweet with invalid data."""
    invalid_data = {
        "result": "Not a boolean",
        "tweets": [
            {
                "id": "invalid-uuid",
                "content": 123,  # Should be a string
                "attachments": "Not a list",
                "author": {
                    "id": "invalid-uuid",
                    "name": 456,  # Should be a string
                },
                "likes": [
                    {
                        "user_id": "invalid-uuid",
                        "name": 789,  # Should be a string
                    },
                ],
            },
        ],
    }

    with pytest.raises(ValidationError):
        ValidGETModelTweet(**invalid_data)


def test_empty_tweets_list() -> None:
    """Test ValidGETModelTweet with an empty tweets list."""
    data = {"result": True, "tweets": []}
    tweets = ValidGETModelTweet(**data)
    assert tweets.result is True
    assert len(tweets.tweets) == 0


def test_multiple_tweets() -> None:
    """Test ValidGETModelTweet with multiple tweets."""
    tweets_data_dict = cast(Dict[str, Any], tweets_data)
    tweets_list = cast(List[Dict[str, Any]], tweets_data_dict["tweets"])

    if tweets_list:
        tweet_data = tweets_list[0]
        multi_tweets_data: Dict[str, Any] = {
            "result": True,
            "tweets": [tweet_data, tweet_data],
        }
        tweets = ValidGETModelTweet(**multi_tweets_data)
        assert tweets.result is True
        assert len(tweets.tweets) == 2
        assert tweets.tweets[0].content == tweets.tweets[1].content
