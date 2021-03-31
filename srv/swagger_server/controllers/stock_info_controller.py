from operator import methodcaller
from swagger_server.models.stock_info_short import StockInfoShort
from swagger_server.constants import DbMarketCode, DbTradeOperation, DbTradeTerm
from swagger_server.services.get_all_tickers import get_all_tickers
from ..exceptions import GetAllTickersInfoIssue, InvalidRequestBody, UserNotFound, EmailAlreadyRegistered, UsernameAlreadyRegistered
from .controller_meta import ControllerMeta
from flask import Response
from connexion import request

class StockInfoController(metaclass=ControllerMeta):

    @classmethod
    def get_stock_info_short_ticker(cls, ticker) -> Response:
        return StockInfoShort().to_dict(), 200
    
