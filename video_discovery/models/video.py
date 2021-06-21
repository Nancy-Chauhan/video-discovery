from ..db import db


class Video(db.Model):
    id = db.Column(db.String(48), primary_key=True)
    video_id = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    thumbnail = db.Column(db.Text(2048), nullable=False)
    published_at = db.Column(db.DateTime(timezone=True), nullable=False, index=True)

    @staticmethod
    def get(message_id):
        return Video.query.get(message_id)
