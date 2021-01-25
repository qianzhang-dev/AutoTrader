from .. import at_db
import sqlalchemy as db


class DbAlert(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("db_user.id"), nullable=False)
    event_type = db.Column(db.NCHAR(16), nullable=False)
    ticker = db.Column(db.NCHAR(16), nullable=False)
    price = db.Column(db.FLOAT, nullable=False)
    created_timestamp = db.Column(db.DateTime, nullable=False)
    deleted_timestamp = db.Column(db.DateTime, nullable=True)
    last_triggered_timestamp = db.Column(db.DateTime, nullable=True)
    last_inspected_timestamp = db.Column(db.DateTime, nullable=True)
