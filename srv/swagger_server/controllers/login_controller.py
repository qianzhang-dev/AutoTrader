from swagger_server.db_models.db_user import DbUser
from typing import List

from connexion import request
from flask import Response

from .controller_meta import ControllerMeta
from ..models import UserResponse
from ..exceptions import UserNotFound

class LoginController(metaclass=ControllerMeta):
    @classmethod
    def post_login(cls) -> Response:
        username = request.authorization.username
        users: List[DbUser] = cls.db.session.query(DbUser).filter(DbUser.username == username).all()
        if not users:
            raise UserNotFound(username, 404)

        user: DbUser = users[0]
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            email_verified=True,
            created_date=user.created_timestamp,
            last_logged_in_date=None
        ).to_dict(), 202
