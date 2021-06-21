from sqlalchemy import desc

from ..db import db


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_id = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    thumbnail_url = db.Column(db.String(2048), nullable=False)
    published_at = db.Column(db.DateTime(timezone=True), nullable=False, index=True)

    @staticmethod
    def get(message_id):
        return Video.query.get(message_id)

    @staticmethod
    def latest():
        return Video.query.order_by(desc(Video.published_at)).limit(1).first()
