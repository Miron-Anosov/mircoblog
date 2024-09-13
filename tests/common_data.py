"""Common data for tests."""

from src.back_core.validators.valid_user import ValidateUserProfile

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

ValidateUserProfile_fake_user_profile = ValidateUserProfile(**user_data)
