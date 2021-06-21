from flask import jsonify
from flask.blueprints import Blueprint
from sqlalchemy import desc

from video_discovery.models.video import Video

blueprint = Blueprint('videos', __name__)


@blueprint.route('', methods=['GET'])
def list_all_videos():
    """
    A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
    """
    data = Video.query.order_by(desc(Video.published_at)).limit(10).all()
    return jsonify(serialize_many(data))


def serialize(video):
    return {
        'id': video.id,
        'title': video.title,
        'description': video.description,
        'thumbnailUrl': video.thumbnail_url,
        'publishedAt': video.published_at.isoformat().replace('+00:00', 'Z'),
    }


def serialize_many(videos):
    return [serialize(video) for video in videos]
