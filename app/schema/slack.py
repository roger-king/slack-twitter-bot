from typing import Dict, List, Any, Optional
from pydantic import BaseModel


class SlackURLVerification(BaseModel):
    token: str
    challenge: str
    type: str


class SlackBlockElement(BaseModel):
    type: str
    text: Optional[str]

    elements: Optional[List[Dict[Any, Any]]]


class SlackBlock(BaseModel):
    type: str
    block_id: str
    elements: List[SlackBlockElement]


class SlackEvent(BaseModel):
    client_msg_id: str
    type: str
    text: str
    user: str
    ts: str
    blocks: List[SlackBlock]
    channel: str
    event_ts: str
    channel_type: str


class SlackEventsResponse(BaseModel):
    token: str
    team_id: str
    api_app_id: str
    type: str
    event: SlackEvent
    event_id: str
    event_time: int
    is_ext_shared_channel: bool
    authorizations: List[Any]
    event_context: str
