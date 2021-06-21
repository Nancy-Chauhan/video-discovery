from dateutil.parser import isoparse
from flask import jsonify, request
from flask.blueprints import Blueprint
from sqlalchemy import desc

from video_discovery.models.video import Video

blueprint = Blueprint('videos', __name__)


def validation_error(message):
    return jsonify({
        'message': 'Validation error',
        'errors': message
    }), 400


@blueprint.route('', methods=['GET'])
def list_all_videos():
    try:
        offset_param = request.args.get('offset')
        offset = isoparse(offset_param) if offset_param else None
    except ValueError:
        return validation_error('"offset" is not a valid date')

    try:
        limit = int(request.args.get('limit', default="10"))
    except ValueError:
        return validation_error('"limit" is not a valid integer')

    search = request.args.get("q")

    query = Video.query

    if search:
        query = query.filter(Video.__ts_vector__.match(search))

    if offset:
        query = query.filter(Video.published_at <= offset)

    data = query.order_by(desc(Video.published_at)).limit(limit).all()
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
