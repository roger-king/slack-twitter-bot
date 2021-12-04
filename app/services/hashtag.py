from app.core import settings


def build_hashtags() -> str:
    hashtag_blob = ''
    for tag in settings.TAGS:
        hashtag_blob += f'#{tag} '

    return hashtag_blob.strip()
