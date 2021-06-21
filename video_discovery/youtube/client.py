import requests
from dateutil.parser import isoparse

from video_discovery import settings


def parse_video(item):
    snippet = item['snippet']
    return {
        'video_id': item['id']['videoId'],
        'title': snippet['title'],
        'description': snippet['description'],
        'thumbnail_url': snippet['thumbnails']['default']['url'],
        'published_at': isoparse(snippet['publishedAt'])
    }


def search(after=None):
    params = {'type': 'video', 'part': 'id,snippet', 'order': 'date',
              'q': settings.youtube_search_query(), 'key': settings.youtube_api_key()}
    if after:
        params['publishedAfter'] = after.isoformat()
    response = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)
    response.raise_for_status()
    return [parse_video(item) for item in response.json()["items"]]
