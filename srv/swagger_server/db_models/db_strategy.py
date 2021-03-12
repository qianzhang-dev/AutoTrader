from swagger_server.constants import DbStockSector, DbStrategyType, DbTradeTerm
from .. import at_db
import sqlalchemy as db


class DbStrategy(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strategy_name = db.Column(db.NCHAR(1024), nullable=False)
    strategy_detail_id = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    strategy_type = db.Column(db.Enum(DbStrategyType), nullable=True)
    created_timestamp = db.Column(db.DateTime, nullable=False)
    last_modified_timestamp = db.Column(db.DateTime, nullable=True)
    is_completed = db.Column(db.Boolean, nullable=False, default=False)

    # overview info for stratgey entries, duplicate in strategy detail table
    ticker = db.Column(db.NCHAR(100), nullable=False)
    term = db.Column(db.Enum(DbTradeTerm), nullable=True)
    cost_basis = db.Column(db.FLOAT(2), nullable=False, default=0.00)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    sector = db.Column(db.Enum(DbStockSector), nullable=False)