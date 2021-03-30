from connexion import request
from flask import Response

from ..db_models import DbStrategy
from swagger_server.exceptions import InvalidRequestBody
from swagger_server.controllers.controller_meta import ControllerMeta
from swagger_server.models.user_request import UserRequest


class StrategyController(metaclass=ControllerMeta):
    @classmethod
    def post_strategy(cls) -> Response:
        if request.is_json:
            body = UserRequest.from_dict(request.get_json())
        else: 
            raise InvalidRequestBody(400)

        strategy = DbStrategy()
        
