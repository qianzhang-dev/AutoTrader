from connexion import request
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from .. import at_db
from ..db_models import DbPingEvent


class DefaultHandler:
    def __init__(self):
        self.db: SQLAlchemy = at_db

    def handle_get_ping(self):
        ping_event = DbPingEvent()
        ping_event.request_timestamp = datetime.now()
        ping_event.user_agent = str(request.user_agent)
        self.db.session.add(ping_event)
        self.db.session.commit()