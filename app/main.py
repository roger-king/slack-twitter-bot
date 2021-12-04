import os
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from app.core import settings
from app.api import api_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title=settings.PROJECT_NAME)
origins = [
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def setup_routers():
    app.include_router(api_router, prefix=settings.API_STR)


def check_env_vars():
    missing_required_envs = []
    if settings.TWITTER_ACCESS_SECRET == None:
        missing_required_envs.append('TWITTER_ACCESS_SECRET')

    if settings.TWITTER_ACCESS_TOKEN == None:
        missing_required_envs.append('TWITTER_ACCESS_TOKEN')

    if settings.TWITTER_CONSUMER_KEY == None:
        missing_required_envs.append('TWITTER_API_KEY')

    if settings.TWITTER_CONSUMER_SECRET == None:
        missing_required_envs.append('TWITTER_API_SECRET_KEY')

    if len(settings.CHANNELS_TO_WATCH) == 0:
        print("no channels set to watch")

    return missing_required_envs


@ app.on_event("startup")
async def startup_event():
    required_vars = check_env_vars()

    if len(required_vars) > 0:
        print(f"missing required environment variables: {required_vars}")
        exit(1)

    setup_routers()
