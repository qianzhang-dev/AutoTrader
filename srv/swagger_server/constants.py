from os import path
import sqlalchemy as db

SWAGGER_SPEC_DIR = path.join(path.dirname(__file__), 'swagger')
SWAGGER_CONFIG = path.join(path.dirname(__file__), 'swagger', 'swagger.yaml')
SWAGGER_URL_PREFIX = '/api-docs'

SQLITE_DB_CONNSTR = 'sqlite:///example.sqlite'

# db common class
class DbTradeOperation(db.Enum):
    NONE = 'none'
    BUY= 'buy'
    SELL = 'sell'

    SELL_COVERED_CALL = 'sell to open covered call'
    EXPIRE_COVERED_CALL = 'covered call expired'
    BUY_COVERED_CALL = 'buy to close covered call'

    BUY_OPEN_CALL = 'buy to open call'
    EXPIRE_CALL = 'call expired'
    SELL_CLOSE_CALL = 'sell to close call'

    BUY_OPEN_PUT = 'buy to open put'
    EXPIRE_PUT = 'put expired'
    SELL_CLOSE_PUT = 'sell to close put'


class DbStockSector(db.Enum):
    BASIC_MATERIALS = 'Basic Materials'
    INDUSTRIALS = 'Industrials'
    FINANCIAL_SERVICES = 'Financial Services'
    ENERGY = 'Energy'
    CONSUMER_CYCLICAL = 'Consumer Cyclical'
    TECHNOLOGY = 'Technology'
    COMMUNICATION_SERVICES = 'Communication Services'
    REAL_ESTATE = 'Real Estate'
    HEALTHCARE = 'Healthcare'
    CONSUMER_DEFENSIVE = 'Consumer Defensive'
    UTILITIES = 'Utilities'


class DbTradeTerm(db.Enum):
    LONG_TERM = 'long term'
    SHORT_TERM = 'short term'
    MIDDLE_TERM = 'middle term'
    FLEX_TERM = 'flex'


class DbStrategyType(db.Enum):
    SPAC = 'SPAC'
    BUY_LOW_SELL_HIGH = '高抛低吸'
    LONG_HOLD = '长持'
    SHORT_HOLD = '短线'
    #DAY_TRADE = '日内'
