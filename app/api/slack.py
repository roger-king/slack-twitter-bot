from typing import Any, Union, Dict

from fastapi import APIRouter

from app.core import settings
from app.schema.slack import SlackURLVerification, SlackEventsResponse
from app.services.twitter import post_tweet

router = APIRouter()


@router.post("", response_model=Any)
def slack_event_listner(input: Union[SlackEventsResponse, SlackURLVerification]) -> Any:
    if isinstance(input, SlackURLVerification):
        return {"challenge": input.challenge}

    channel = input.event.channel
    if len(settings.CHANNELS_TO_WATCH) > 0 and channel in settings.CHANNELS_TO_WATCH:
        channel_type = input.event.channel_type
        if channel_type == 'channel' or channel_type == 'group':
            print("posting tweet")
            post_tweet(input.event.text)
        return True

    return False
