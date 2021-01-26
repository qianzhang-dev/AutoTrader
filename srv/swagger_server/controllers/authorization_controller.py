import bcrypt

from .. import at_db
from ..exceptions import AuthorizationFailure
from ..db_models import DbUser

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_basic_authorization(username: str, password: str, required_scopes):
    if not username or not password:
        raise AuthorizationFailure(username, 401)

    matched_users = at_db.session.query(DbUser).filter(DbUser.username == username.lower()).all()
    if not matched_users:
        raise AuthorizationFailure(username, 401)

    user = matched_users[0]
    if not bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        raise AuthorizationFailure(username, 401)

    return {'user_id': user.id}


