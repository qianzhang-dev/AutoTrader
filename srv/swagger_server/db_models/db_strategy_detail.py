from enum import Enum
from swagger_server.constants import DbTradeOperation
from .. import at_db
import sqlalchemy as db


class DbStrategyDetail(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strategy_id = db.Column(db.Integer, nullable=False)
    cur_cost_basis = db.Column(db.FLOAT(2), nullable=False, default=0.00)
    cur_quantity = db.Column(db.Integer, nullable=False, default=0)
    created_timestamp = db.Column(db.DateTime, nullable=False)
    last_modified_timestamp = db.Column(db.DateTime, nullable=True)

    operation = db.Column(db.Enum(DbTradeOperation), nullable=False)
    price = db.Column(db.FLOAT(2), nullable=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    commentId = db.Column(db.Integer, nullable=True)
