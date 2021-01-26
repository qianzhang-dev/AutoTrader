from flask import Response

from .controller_meta import ControllerMeta


class LoginController(metaclass=ControllerMeta):
    @classmethod
    def post_login(cls) -> Response:
        return Response(response='Accepted', status=202)
