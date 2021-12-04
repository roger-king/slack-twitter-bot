from pytwitter import Api
from app.core import settings


def post_tweet(text: str):
    api = Api(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token=settings.TWITTER_ACCESS_TOKEN,
        access_secret=settings.TWITTER_ACCESS_SECRET
    )
    api.create_tweet(text=text)
