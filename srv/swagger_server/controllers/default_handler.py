from typing import List
from datetime import datetime
from swagger_server.db_models.db_alert import DbAlert

from swagger_server.db_models.db_user import DbUser
from connexion import request
from flask_sqlalchemy import SQLAlchemy
import bcrypt


from .. import at_db
from ..exceptions import (
    AlertNotFound,
    EmailAlreadyRegistered,
    UserNotFound,
    AlertAlreadyCreated
)
from ..models import Body2, Body1, Body
from ..db_models import DbPingEvent, DbUser, DbAlert


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
    
    def handle_get_users_user_id(self, user_id: int) -> DbUser:
        users = self.db.session.query(DbUser).filter(DbUser.id == user_id).all()
        if not users:
            raise UserNotFound(str(user_id))
        return users[0]

    def handle_patch_users_user_id(self, user_id: int, body: Body) -> DbUser:
        users = self.db.session.query(DbUser).filter(DbUser.id == user_id).all()
        if not users:
            raise UserNotFound(str(user_id))
        
        # Update user
        user = users[0]
        if body.username:
            user.username = body.username
        if body.email:
            user.email = body.email
        if body.password:
            salt_bytes = bcrypt.gensalt()
            password_bytes = bcrypt.hashpw(body.password.encode('utf-8'), salt_bytes)
            user.password_salt = salt_bytes.decode('utf-8')
            user.password_hash = password_bytes.decode('utf-8')
        
        # Add to db_user table
        self.db.session.flush()
        self.db.session.commit()

        # Get result user
        self.db.session.refresh(user)
        return user
    
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

        # Add to db_user table
        self.db.session.add(user)
        self.db.session.flush()
        self.db.session.commit()

        # Get result user
        self.db.session.refresh(user)
        return user
    
    def handle_post_users_user_id_alert(self, user_id: int, body: Body2) -> DbAlert:
        # Validate if user exist
        matched_users = self.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id)
            
        # Validate if alert already exist
        validated_user_id = matched_users[0].id
        matched_alerts = self.db.session.query(DbAlert.id) \
                                        .filter(DbAlert.owner_id == validated_user_id) \
                                        .filter(DbAlert.ticker == body.ticker.lower()) \
                                        .filter(DbAlert.event_type == body.event_type.lower()) \
                                        .filter(DbAlert.price == body.price) \
                                        .all()
        if matched_alerts:
            created_alert_id = matched_alerts[0].id
            raise AlertAlreadyCreated(body.ticker.lower(), body.event_type.lower(), body.price, created_alert_id)
            
        # Create new alert
        alert = DbAlert()
        alert.created_timestamp = datetime.now()
        alert.owner_id = user_id
        alert.price = body.price
        alert.ticker = body.ticker.lower()
        alert.event_type = body.event_type.lower()

        # Add to db_alert table
        self.db.session.add(alert)
        self.db.session.flush()
        self.db.session.commit()

        # Get result alert
        self.db.session.refresh(alert)
        return alert
    
    def handle_get_users_user_id_alerts(self, user_id: int) -> List[DbAlert]:
        # Validate if user exist
        matched_users = self.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id)
            
        # Get all alerts
        validated_user_id = matched_users[0].id
        matched_alerts = self.db.session.query(DbAlert).filter(DbAlert.owner_id == validated_user_id).all()
        return list(matched_alerts)
    
    def handle_get_users_user_id_alerts_ticker(self, user_id: int, ticker: str) -> List[DbAlert]:
        # Validate if user exist
        matched_users = self.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id)
            
        # Validate if ticker exist
        validated_user_id = matched_users[0].id
        matched_alerts = self.db.session.query(DbAlert) \
                                        .filter(DbAlert.owner_id == validated_user_id) \
                                        .filter(DbAlert.ticker == ticker.lower()) \
                                        .all()
        return list(matched_alerts)
    
    def get_users_user_id_alerts_ticker_alert_id(self, user_id: int, ticker: str, id: int) -> DbAlert:
        # Validate if user exist
        matched_users = self.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id)

        # Validate if ticker exist
        validated_user_id = matched_users[0].id
        matched_alerts = self.db.session.query(DbAlert) \
                                        .filter(DbAlert.owner_id == validated_user_id) \
                                        .filter(DbAlert.ticker == ticker.lower()) \
                                        .filter(DbAlert.id == id) \
                                        .all()
        
        if not matched_alerts:
            raise AlertNotFound(id)
            
        return matched_alerts[0]