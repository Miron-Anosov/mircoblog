"""Test API routes."""

from typing import cast
from unittest.mock import AsyncMock, create_autospec, patch

import pytest

from src.back_core.controllers.tweets_controllers.del_like_tweet import (
    del_like_tweet_by_id,
)
from src.back_core.controllers.tweets_controllers.del_tweet import (
    del_tweet_by_id,
)
from src.back_core.controllers.tweets_controllers.get_tweets import get_tweets
from src.back_core.controllers.tweets_controllers.post_like_tweet import (
    post_like_by_id,
)
from src.back_core.controllers.tweets_controllers.post_new_tweet import (
    post_new_tweet,
)
from src.back_core.controllers.users_controllers.users import (
    follow_users,
    follow_users_delete,
    get_user_profile,
    get_user_profile_by_id,
)
from src.back_core.validators.valid_user import ValidateUserProfile
from tests.common_data import tweets_data, user_data


@pytest.mark.asyncio
@pytest.mark.mock
async def test_get_user_profile_with_mocked_data_and_api_key():
    """Test func with moke."""
    mocked_profile = ValidateUserProfile(**user_data)
    trg = "src.back_core.controllers.users_controllers.users.get_user_profile"
    with patch(
        target=trg,
        return_value=mocked_profile,
        new_callable=AsyncMock,
    ) as mock_func:
        result = await mock_func(api_key="test-key")
        assert result == mocked_profile, f"Validation error: {result}"


@pytest.mark.asyncio
@pytest.mark.mock
async def test_get_user_profile() -> None:
    """Test too many positional arguments."""
    mock_user_prof = create_autospec(
        get_user_profile,
        return_value=AsyncMock(return_value=user_data),
    )
    assert await cast(AsyncMock, mock_user_prof)()
    with pytest.raises(TypeError):
        assert cast(AsyncMock, mock_user_prof)("argument")


@pytest.mark.asyncio
@pytest.mark.mock
async def test_follow_users_delete() -> None:
    """Test too many positional arguments."""
    mock_follow_users_delete = create_autospec(
        follow_users_delete, return_value=user_data
    )
    with pytest.raises(TypeError):
        assert mock_follow_users_delete()
    assert await mock_follow_users_delete(user_id="any_user_id_str")


@pytest.mark.asyncio
@pytest.mark.mock
async def test_follow_users() -> None:
    """Test too many positional arguments."""
    mock_follow_users = create_autospec(follow_users, return_value=user_data)
    with pytest.raises(TypeError):
        assert await mock_follow_users()
    assert await mock_follow_users(user_id="any_user_id_str")


@pytest.mark.asyncio
@pytest.mark.mock
async def test_get_user_profile_by_id() -> None:
    """Test too many positional arguments."""
    mock_get_user_profile_by_id = create_autospec(
        get_user_profile_by_id, return_value=user_data
    )
    assert await mock_get_user_profile_by_id(id_="any_user_id_str")
    with pytest.raises(TypeError):
        assert await mock_get_user_profile_by_id()


@pytest.mark.asyncio
@pytest.mark.mock
async def test_get_tweets() -> None:
    """Test too many positional arguments."""
    mock_get_tweets = create_autospec(get_tweets, return_valume=tweets_data)
    assert await mock_get_tweets()
    with pytest.raises(TypeError):
        assert await mock_get_tweets("any_user_id_str")


@pytest.mark.asyncio
@pytest.mark.mock
async def test_del_tweet_by_id() -> None:
    """Test too many positional arguments."""
    mock_del_tweet_by_id = create_autospec(
        del_tweet_by_id, return_valume=tweets_data
    )
    assert await mock_del_tweet_by_id(tweet_id="any_user_id_str")
    with pytest.raises(TypeError):
        assert await mock_del_tweet_by_id()


@pytest.mark.asyncio
@pytest.mark.mock
async def test_post_new_tweet() -> None:
    """Test too many positional arguments."""
    mock_post_new_tweet = create_autospec(
        post_new_tweet, return_valume=tweets_data
    )
    assert await mock_post_new_tweet(tweet="any_user_id_str")
    with pytest.raises(TypeError):
        assert await mock_post_new_tweet()


@pytest.mark.asyncio
@pytest.mark.mock
async def test_post_like_by_id() -> None:
    """Test too many positional arguments."""
    mock_post_like_by_id = create_autospec(
        post_like_by_id, return_valume=tweets_data
    )
    assert await mock_post_like_by_id(tweet_id="any_user_id_str")
    with pytest.raises(TypeError):
        assert await mock_post_like_by_id()
        assert await mock_post_like_by_id(tweet_iD="any_user_id_str")


@pytest.mark.asyncio
@pytest.mark.mock
async def test_del_like_tweet_by_id() -> None:
    """Test too many positional arguments."""
    mock_del_like_tweet_by_id = create_autospec(
        del_like_tweet_by_id, return_valume=tweets_data
    )
    assert await mock_del_like_tweet_by_id(tweet_id="any_user_id_str")
    with pytest.raises(TypeError):
        assert await mock_del_like_tweet_by_id()
        assert await mock_del_like_tweet_by_id(tweet_iD="any_user_id_str")
