from enum import Enum
from .. import at_db
import sqlalchemy as db


class DbStrategyComment(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strategy_detail_id = db.Column(db.Integer, nullable=False)
    strategy_id = db.column(db.Integer, nullable=False)
    created_timestamp = db.Column(db.DateTime, nullable=False)
    last_modified_timestamp = db.Column(db.DateTime, nullable=True)

    comment = db.Column(db.NCHAR(1024), nullable=True)
