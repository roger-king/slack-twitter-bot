from pytwitter import Api
from app.core import settings
from app.services.hashtag import build_hashtags


def post_tweet(text: str):
    api = Api(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token=settings.TWITTER_ACCESS_TOKEN,
        access_secret=settings.TWITTER_ACCESS_SECRET
    )
    complete_tweet = f'{text} {build_hashtags()}'

    if len(complete_tweet) <= 280:
        api.create_tweet(text=complete_tweet)
    else:
        print("tweet is too long: {text}")
