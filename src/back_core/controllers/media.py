"""Media work this user pictures."""

from fastapi import APIRouter

media = APIRouter(prefix="/api", tags=["Media"])


@media.post("/media")
def get_status():
    """Test route."""
    return {"message": "Hello World"}
