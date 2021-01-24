from os import path

import connexion
from connexion.apps.flask_app import FlaskApp

from flask_sqlalchemy import SQLAlchemy

from swagger_server import encoder
from swagger_ui import flask_api_doc

from .constants import SWAGGER_CONFIG, SWAGGER_URL_PREFIX, SWAGGER_SPEC_DIR, SQLITE_DB_CONNSTR


def main():
    app_ = connexion.App(__name__, specification_dir=SWAGGER_SPEC_DIR)
    app_.app.json_encoder = encoder.JSONEncoder
    app_.add_api('swagger.yaml', arguments={'title': 'AutoTrader'}, pythonic_params=True)
    flask_api_doc(app_.app, config_path=SWAGGER_CONFIG, url_prefix=SWAGGER_URL_PREFIX)
    app_.run(port=3000)

cnx = connexion.App(__name__, specification_dir=SWAGGER_SPEC_DIR)
cnx.app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_CONNSTR
cnx.app.json_encoder == encoder.JSONEncoder

db = SQLAlchemy(cnx.app)
from . import db_models

cnx.add_api('swagger.yaml', arguments={'title': 'AutoTrader'}, pythonic_params=True)
flask_api_doc(cnx.app, config_path=SWAGGER_CONFIG, url_prefix=SWAGGER_URL_PREFIX)
