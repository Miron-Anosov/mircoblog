"""There are all API controllers.

Controllers:
    - tweets
    - users
    - media
"""

from src.back_core.controllers.media_controllers.media import media
from src.back_core.controllers.tweets_controllers.main_tweets import tweets
from src.back_core.controllers.users_controllers.users import users
from src.back_core.settings import swagger_info

__all__ = ["users", "tweets", "media", "swagger_info"]
