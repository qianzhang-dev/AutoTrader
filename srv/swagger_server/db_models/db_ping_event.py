from .. import at_db
import sqlalchemy as db


class DbPingEvent(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_timestamp = db.Column(db.DateTime, nullable=False)
    user_agent = db.Column(db.NCHAR(1024), nullable=False)
