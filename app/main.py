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


@app.on_event("startup")
async def startup_event():
    setup_routers()
