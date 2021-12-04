from fastapi import APIRouter

from app.api import status
from app.api import slack

api_router = APIRouter()
api_router.include_router(
    status.router, prefix="/status", tags=["status"])
api_router.include_router(slack.router, prefix="/slack", tags=["slack"])
