from connexion import request
from datetime import datetime
from .. import at_db
from ..db_models import DbPingEvent


class DefaultHandler:

    @staticmethod
    def handle_get_ping():
        ping_event = DbPingEvent()
        ping_event.request_timestamp = datetime.now()
        ping_event.user_agent = str(request.user_agent)
        at_db.session.add(ping_event)
        at_db.session.commit()