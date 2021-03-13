from enum import Enum
from swagger_server.constants import DbTradeOperation
from .. import at_db
import sqlalchemy as db

class DbStrategyActivity(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strategy_id = db.Column(db.Integer, db.ForeignKey("db_strategy.id"), nullable=False)
    created_timestamp = db.Column(db.DateTime, nullable=False)
    last_modified_timestamp = db.Column(db.DateTime, nullable=True)

    operator = db.Column(db.Enum(DbTradeOperation), nullable=False)
    comment = db.Column(db.NCHAR(1024), nullable=True)
    
    # operator:: buy or sell
    price = db.Column(db.FLOAT(2), nullable=True)
    quantity = db.Column(db.Integer, nullable=True, default=0)

    # operator:: change goal
    target_prices = db.Column(db.PickleType, nullable=True)
    stop_loss_prices = db.Column(db.PickleType, nullable=True)
