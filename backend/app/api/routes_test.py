from fastapi import APIRouter

# Create a router for simple health-check endpoints
router = APIRouter()

@router.get("/ping")
def ping():
    """
    Simple health check endpoint.

    Purpose:
    - Allows the frontend or deployment environment to confirm
      that the backend server is running properly.
    - Useful during local development, CI checks, Docker health probes, etc.

    Returns:
    - A small JSON message indicating the API is active.
    """
    return {"message": "Backend up & running!"}