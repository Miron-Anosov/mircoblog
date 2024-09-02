"""Media work this user pictures."""

from fastapi import APIRouter

media = APIRouter(tags=["Media"])


@media.post("/media")
async def get_status() -> dict[str, str]:
    """Test route."""
    return {"message": "Hello World"}
