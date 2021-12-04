# slack-twitter-bot

A simple python service to listen to a slack channel and tweet it text.

# Usage

_Note_: This will tweet everything in the desired channels. It will not ignore replies (threads) or direct message or reply in thread.

Some fun ideas this can be used for:

- Tweeting updates about a service outage. This can be consolidated to relay from your slack alerts.

## Environment variables:

| ENV_NAME  | VALUE | DESCRIPTION  | REQUIRED |
| ------------- | ------------- | ------------- | ------------- |
|  TWITTER_API_KEY | string  | Twitter Consumer API Key  | True |
|  TWITTER_API_SECRET_KEY | string  | Twitter Consumer Secret Key  | True |
|  TWITTER_ACCESS_TOKEN | string  | Twitter Access Token  | True |
|  TWITTER_ACCESS_SECRET | string  | Twitter Access Secret Key  | True |
|  SLACK_CHANNELS | comma-separated string  | Slack Channel IDs you wish the service to listen to. | True |
|  HASHTAGS | comma-separated string  | Hashtags you wish to append to the tweet. | False |

## Development

### Pre-requisites

- Python3.9.8^
- set `.env` file with above environment variables
- Poetry dependency management
- Slack App and endpoint configured to `http://{host}/api/slack`
- Twitter Application keys configured

```bash
    poetry run python run.py
```

## Future Features

- Retweet reply responses from a thread to original post.