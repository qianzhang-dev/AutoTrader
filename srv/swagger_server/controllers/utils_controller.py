from operator import methodcaller
from swagger_server.constants import DbMarketCode, DbStockSector, DbStrategyType, DbTradeOperation, DbTradeTerm
from swagger_server.services.get_all_tickers import get_all_tickers
from ..exceptions import GetAllTickersInfoIssue, InvalidRequestBody, UserNotFound, EmailAlreadyRegistered, UsernameAlreadyRegistered
from .controller_meta import ControllerMeta
from flask import Response
from connexion import request

class UtilsController(metaclass=ControllerMeta):
    
    
    @classmethod
    def get_investment_terms(cls) -> Response:
        return [term.value for term in DbTradeTerm], 200
    
    @classmethod
    def get_market_codes(cls) -> Response:
        return [code.value for code in DbMarketCode], 200
    
    @classmethod
    def get_trade_operators(cls) -> Response:
        return [op.value for op in DbTradeOperation], 200
    
    @classmethod
    def get_sectors(cls) -> Response:
        return [sector.value for sector in DbStockSector], 200
    
    @classmethod
    def get_strategies(cls) -> Response:
        return [strategy.value for strategy in DbStrategyType], 200
    
    

