from operator import methodcaller
from swagger_server.services.get_all_tickers import get_all_tickers
from ..exceptions import GetAllTickersInfoIssue, InvalidRequestBody, UserNotFound, EmailAlreadyRegistered, UsernameAlreadyRegistered
from .controller_meta import ControllerMeta

class TickerController(metaclass=ControllerMeta):
    @classmethod
    def get_get_all_tickers_and_sectors(cls):
        try:
            get_all_tickers(cls)
        except:
            raise GetAllTickersInfoIssue('')
        return "All tickers and related info generated."
