from typing import Dict
from datetime import datetime

from connexion import request
from flask import Response

from ..exceptions import AlertNotFound, InvalidRequestBody, UserNotFound, AlertAlreadyCreated
from ..models import AlertRequest, AlertResponse
from ..db_models import DbAlert, DbUser
from .controller_meta import ControllerMeta


class AlertController(metaclass=ControllerMeta):
    @classmethod
    def get_users_user_id_alerts(self, user_id: int) -> Response:
        # Validate if user exist
        matched_users = self.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id, 404)
            
        # Get all alerts
        validated_user_id = matched_users[0].id
        matched_alerts = self.db.session.query(DbAlert).filter(DbAlert.owner_id == validated_user_id).all()
        return [AlertResponse(
           id=ma.id,
           owner_id=ma.owner_id,
           event_type=ma.event_type,
           disabled=ma.deleted_timestamp is not None,
           created_time=ma.created_timestamp,
           last_triggered_time=ma.last_triggered_timestamp,
           price=ma.price,
           ticker=ma.ticker 
        ).to_dict() for ma in matched_alerts], 200

    @classmethod
    def post_users_user_id_alert(cls, user_id: int, body: Dict) -> Response:
        # General parsing check
        if request.is_json:
            body = AlertRequest.from_dict(request.get_json())
        else:
            raise InvalidRequestBody(400)

        # Validate if user exist
        matched_users = cls.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id, 404)
            
        # Validate if alert already exist
        validated_user_id = matched_users[0].id
        matched_alerts = cls.db.session.query(DbAlert.id) \
                                       .filter(DbAlert.owner_id == validated_user_id) \
                                       .filter(DbAlert.ticker == body.ticker.lower()) \
                                       .filter(DbAlert.event_type == body.event_type.lower()) \
                                       .filter(DbAlert.price == body.price) \
                                       .all()
        if matched_alerts:
            created_alert_id = matched_alerts[0].id
            raise AlertAlreadyCreated(ticker=body.ticker.lower(),
                                      event_type=body.event_type.lower(),
                                      price=body.price,
                                      id=created_alert_id,
                                      error_code=409)
            
        # Create new alert
        alert = DbAlert()
        alert.created_timestamp = datetime.now()
        alert.owner_id = user_id
        alert.price = body.price
        alert.ticker = body.ticker.lower()
        alert.event_type = body.event_type.lower()

        # Add to db_alert table
        cls.db.session.add(alert)
        cls.db.session.flush()
        cls.db.session.commit()

        # Get result alert
        cls.db.session.refresh(alert)
        return AlertResponse(
            id=alert.id,
            owner_id=alert.owner_id,
            event_type=alert.event_type,
            disabled=alert.deleted_timestamp is not None,
            created_time=alert.created_timestamp,
            last_triggered_time=alert.last_triggered_timestamp,
            price=alert.price,
            ticker=alert.ticker 
        ).to_dict(), 201

    @classmethod
    def get_users_user_id_alerts_ticker_alert_id(cls, user_id: int, ticker: str, alert_id: int) -> Response:
        # Validate if user exist
        matched_users = cls.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id, 404)

        # Validate if ticker exist
        validated_user_id = matched_users[0].id
        matched_alerts = cls.db.session.query(DbAlert) \
                                        .filter(DbAlert.owner_id == validated_user_id) \
                                        .filter(DbAlert.ticker == ticker.lower()) \
                                        .filter(DbAlert.id == alert_id) \
                                        .all()
        
        if not matched_alerts:
            raise AlertNotFound(alert_id)
        
        alert = matched_alerts[0]
        return AlertResponse(
            id=alert.id,
            owner_id=alert.owner_id,
            event_type=alert.event_type,
            disabled=alert.deleted_timestamp is not None,
            created_time=alert.created_timestamp,
            last_triggered_time=alert.last_triggered_timestamp,
            price=alert.price,
            ticker=alert.ticker 
        ).to_dict(), 200
    
    @classmethod
    def get_users_user_id_alerts_ticker(cls, user_id: int, ticker: str) -> Response:
        # Validate if user exist
        matched_users = cls.db.session.query(DbUser.id).filter(DbUser.id == user_id).all()
        if not matched_users:
            raise UserNotFound(user_id)
            
        # Validate if ticker exist
        validated_user_id = matched_users[0].id
        matched_alerts = cls.db.session.query(DbAlert) \
                                        .filter(DbAlert.owner_id == validated_user_id) \
                                        .filter(DbAlert.ticker == ticker.lower()) \
                                        .all()

        return [AlertResponse(
           id=ma.id,
           owner_id=ma.owner_id,
           event_type=ma.event_type,
           disabled=ma.deleted_timestamp is not None,
           created_time=ma.created_timestamp,
           last_triggered_time=ma.last_triggered_timestamp,
           price=ma.price,
           ticker=ma.ticker 
        ).to_dict() for ma in matched_alerts], 200