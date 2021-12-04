import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "FastAPI"
    CHANNELS_TO_WATCH: list[str] = [] if len(os.getenv(
        "SLACK_CHANNELS", "")) == 0 else os.getenv("SLACK_CHANNELS", "").split(",")
    TWITTER_CONSUMER_KEY: str = os.getenv("TWITTER_API_KEY")
    TWITTER_CONSUMER_SECRET: str = os.getenv("TWITTER_API_SECRET_KEY")
    TWITTER_ACCESS_TOKEN: str = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET: str = os.getenv("TWITTER_ACCESS_SECRET")
    TAGS: list[str] = [] if len(os.getenv(
        "HASHTAGS", "")) == 0 else os.getenv("HASHTAGS", "").split(",")

    class Config:
        env_file = ".env"


settings = Settings()
