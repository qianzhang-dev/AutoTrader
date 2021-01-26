from datetime import datetime

from connexion import request
from flask import Response

from ..db_models import DbPingEvent
from .controller_meta import ControllerMeta


class PingController(metaclass=ControllerMeta):
    @classmethod
    def get_ping(cls) -> Response:
        ping_event = DbPingEvent()
        ping_event.request_timestamp = datetime.now()
        ping_event.user_agent = str(request.user_agent)
        cls.db.session.add(ping_event)
        cls.db.session.flush()
        cls.db.session.commit()
        return Response(response='OK', status=200)