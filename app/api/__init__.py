from fastapi import APIRouter

from app.api import status

api_router = APIRouter()
api_router.include_router(
    status.router, prefix="/status", tags=["status"])
