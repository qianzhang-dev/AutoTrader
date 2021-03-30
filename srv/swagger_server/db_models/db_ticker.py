from swagger_server.constants import DbMarketCode, DbStockSector
from .. import at_db
import sqlalchemy as db


class DbTicker(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.NCHAR(10), nullable=False)
    currency = db.Column(db.NCHAR(10), nullable=False)
    market_code = db.Column(db.Enum(DbMarketCode), nullable=False)
    name = db.Column(db.NCHAR(1024), nullable=False)
    description = db.Column(db.NCHAR(1024), nullable=True)
    sector = db.Column(db.Enum(DbStockSector), nullable=False)
    
