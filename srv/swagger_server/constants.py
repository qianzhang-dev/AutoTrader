from os import path
import sqlalchemy as db
import enum

SWAGGER_SPEC_DIR = path.join(path.dirname(__file__), 'swagger')
SWAGGER_CONFIG = path.join(path.dirname(__file__), 'swagger', 'swagger.yaml')
SWAGGER_URL_PREFIX = '/api-docs'

SQLITE_DB_CONNSTR = 'sqlite:///example.sqlite'

# db common class
class DbTradeOperation(enum.Enum):
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

    CHANGE_TARGET_PRICES = 'change target price'
    CHANGE_STOP_LOSS_PRICES = 'change stop loss price'

    DIVIDEND_EARNING = 'dividend earning'


class DbStockSector(enum.Enum):
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


class DbTradeTerm(enum.Enum):
    LONG_TERM = 'long term'
    SHORT_TERM = 'short term'
    MIDDLE_TERM = 'middle term'
    FLEX_TERM = 'flex'


class DbStrategyType(enum.Enum):
    SPAC = 'SPAC'
    BUY_LOW_SELL_HIGH = 'General buy low sell high'
    LONG_HOLD = 'Long term holding'
    SHORT_HOLD = 'Short term holding'
    DAY_TRADE = 'Day trade'
    DIVIDEND_INVESTMENT = 'Divdend investment'


