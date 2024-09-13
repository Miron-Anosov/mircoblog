"""Common data for tests."""

user_data = {
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
