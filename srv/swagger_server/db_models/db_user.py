from .. import at_db
import sqlalchemy as db


class DbUser(at_db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.NCHAR(255), nullable=True)
    email = db.Column(db.NCHAR(255), nullable=False)
    password_hash = db.Column(db.NCHAR(255), nullable=False)
    password_salt = db.Column(db.NCHAR(255), nullable=False)
    created_timestamp = db.Column(db.DateTime, nullable=False)
    last_login_timestamp = db.Column(db.DateTime, nullable=True)
    is_disabled = db.Column(db.Boolean, nullable=False, default=False)
