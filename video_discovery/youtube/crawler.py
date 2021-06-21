from video_discovery import db
from video_discovery.models.video import Video
from video_discovery.youtube.client import search


def run():
    latest = Video.latest()
    videos = search() if latest is None else search(after=latest.published_at)
    with db.transaction():
        for video_info in videos:
            video = Video(**video_info)
            db.persist(video)
