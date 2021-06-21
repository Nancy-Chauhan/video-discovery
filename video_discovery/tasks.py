from celery import Celery

from . import settings
from .wsgi import app as flask_app
from .youtube import crawler

app = Celery('tasks', broker=settings.celery_broker_uri())

app.conf.beat_schedule = {
    'update-youtube-videos': {
        'task': 'video_discovery.tasks.update_youtube_videos',
        'schedule': settings.video_crawl_interval_seconds()
    },
}


@app.task
def update_youtube_videos():
    with flask_app.app_context():
        crawler.run()
