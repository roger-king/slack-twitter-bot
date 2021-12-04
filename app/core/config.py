import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "FastAPI"

    class Config:
        env_file = ".env"


settings = Settings()
