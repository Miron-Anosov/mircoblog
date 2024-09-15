"""Common data for tests."""

valid_user_data = {
    "result": True,
    "user": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f6afa62",
        "name": "Dick",
        "followers": [
            {
                "id": "3fa33364-5717-4562-b3fc-2c963f6afa64",
                "name": "Tom",
            }
        ],
        "following": [
            {
                "id": "3fa33364-5717-4562-b3fc-2c963f4563fa",
                "name": "Ramil",
            }
        ],
    },
}

valid_user_profile = {
    "id": "3fa85f64-5717-4562-b3fc-2c963f6afa62",
    "name": "Dick",
    "followers": [],
    "following": [],
}

invalid_user_profile = {
    "id": "3fa85f64-5717-4562-b3fc-2c963f6afa62",
    "name": "Dick",
    "followers": [],
    # "following": [
    # ],
}

valid_user_model = {
    "id": "3fa85f64-5717-4562-b3fc-2c963f6afa62",
    "name": "Dick",
}
invalid_user_model = {
    "id": "3fa85f64-5717-4562-b3fc-2c963f6afa62",
    # "name": "Dick",
}


tweets_data = {
    "result": True,
    "tweets": [
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "content": "This is a sample tweet",
            "attachments": [
                "/media/images/12345.jpg",
                "/media/images/12346.jpg",
            ],
            "author": {
                "id": "3fa85f64-4578-4562-b3fc-2c963f66afa6",
                "name": "Author Name",
            },
            "likes": [
                {
                    "user_id": "3fa85f64-5555-4562-b3fc-2c963f66afa6",
                    "name": "User1",
                },
            ],
        },
    ],
}

invalid_data_tweet = {
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

invalid_tweet = {
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
}

valid_tweet = {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "content": "This is a sample tweet",
    "attachments": [
        "/media/images/12345.jpg",
        "/media/images/12346.jpg",
    ],
    "author": {
        "id": "3fa85f64-4578-4562-b3fc-2c963f66afa6",
        "name": "Author Name",
    },
    "likes": [
        {
            "user_id": "3fa85f64-5555-4562-b3fc-2c963f66afa6",
            "name": "User1",
        },
    ],
}

invalid_user_data = {
    "result": "Not a boolean",
    "user": {
        "name": "Dick",
        # Empty id
        "followers": [],
        "following": [],
    },
}

invalid_post_new_tweet_response = {
    "result": True,
    "tweet_id": "3fa85f64-5555-4562-b3fc-2c963f66af6",  # invalid uuid
}

valid_post_new_tweet_response = {
    "result": True,
    "tweet_id": "3fa85f64-5555-4562-b3fc-2c963f66afa6",
}
