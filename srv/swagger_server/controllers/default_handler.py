from datetime import datetime

from swagger_server.db_models.db_user import DbUser
from connexion import request
from flask_sqlalchemy import SQLAlchemy
import bcrypt


from .. import at_db
from ..exceptions import EmailAlreadyRegistered
from ..models import Body1
from ..db_models import DbPingEvent, DbUser


class DefaultHandler:
    def __init__(self):
        self.db: SQLAlchemy = at_db

    def handle_get_ping(self):
        ping_event = DbPingEvent()
        ping_event.request_timestamp = datetime.now()
        ping_event.user_agent = str(request.user_agent)
        self.db.session.add(ping_event)
        self.db.session.flush()
        self.db.session.commit()
    
    def handle_post_user(self, body: Body1) -> DbUser:
        # Validate if email is colided
        collided = self.db.session.query(DbUser).filter(DbUser.email == body.email.lower()).all()
        if collided:
            raise EmailAlreadyRegistered(body.email.lower())
        
        # Create new user
        user = DbUser()
        user.created_timestamp = datetime.now()
        user.is_disabled = False
        user.username = body.username.lower()
        user.email = body.email.lower()

        # Generate salt bytes
        salt_bytes = bcrypt.gensalt()
        password_bytes = bcrypt.hashpw(body.password.encode('utf-8'), salt_bytes)
        user.password_salt = salt_bytes.decode('utf-8')
        user.password_hash = password_bytes.decode('utf-8')

        # Add to db user table
        self.db.session.add(user)
        self.db.session.flush()
        self.db.session.commit()

        # Get result user
        self.db.session.refresh(user)

        return user