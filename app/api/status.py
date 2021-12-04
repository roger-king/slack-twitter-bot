from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("", response_model=bool)
def read_server_status() -> Any:
    return True
