from typing import List, Dict
from datetime import datetime

from connexion import request
from flask import Response
import bcrypt

from ..models import UserRequest, UserResponse
from ..db_models import DbUser
from ..exceptions import InvalidRequestBody, UserNotFound, EmailAlreadyRegistered
from .controller_meta import ControllerMeta


class UserController(metaclass=ControllerMeta):
    @classmethod
    def get_users_user_id(cls, user_id: int) -> Response:
        users: List[DbUser] = cls.db.session.query(DbUser).filter(DbUser.id == user_id).all()
        if not users:
            raise UserNotFound(user_id, 404)

        user: DbUser = users[0]
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            email_verified=True,
            created_date=user.created_timestamp,
            last_logged_in_date=None
        ).to_dict(), 200
    
    @classmethod
    def post_user(cls, body: Dict) -> Response:
        # General parsing check
        if request.is_json:
            body = UserRequest.from_dict(request.get_json())
        else:
            raise InvalidRequestBody(400)

        # Validate if email is colided
        collided: List[DbUser] = cls.db.session.query(DbUser).filter(DbUser.email == body.email.lower()).all()
        if collided:
            raise EmailAlreadyRegistered(body.email.lower(), 409)
        
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
        cls.db.session.add(user)
        cls.db.session.flush()
        cls.db.session.commit()

        # Get result user
        cls.db.session.refresh(user)
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            email_verified=True,
            created_date=user.created_timestamp,
            last_logged_in_date=None
        ).to_dict(), 200

    @classmethod
    def patch_users_user_id(cls, user_id: int, body: Dict) -> Response:
        # General parsing check
        if request.is_json:
            body = UserRequest.from_dict(request.get_json())
        else:
            raise InvalidRequestBody(400)

        # Validate if user exists
        users = cls.db.session.query(DbUser).filter(DbUser.id == user_id).all()
        if not users:
            raise UserNotFound(user_id, 404)
        
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
        cls.db.session.flush()
        cls.db.session.commit()

        # Get result user
        cls.db.session.refresh(user)
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            email_verified=True,
            created_date=user.created_timestamp,
            last_logged_in_date=None
        ).to_dict(), 200
