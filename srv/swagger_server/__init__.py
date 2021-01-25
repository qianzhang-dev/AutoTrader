import inspect
import connexion

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from swagger_server import encoder
from swagger_ui import flask_api_doc

from .constants import (
    SWAGGER_CONFIG,
    SWAGGER_URL_PREFIX,
    SWAGGER_SPEC_DIR,
    SQLITE_DB_CONNSTR
)
from . import exceptions

cnx = connexion.App(__name__, specification_dir=SWAGGER_SPEC_DIR)
cnx.app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_CONNSTR
cnx.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

cnx.app.json_encoder == encoder.JSONEncoder

# Register exception handlers from .exceptions module
for name, obj in inspect.getmembers(exceptions):
    if inspect.isclass(obj) and issubclass(obj, connexion.exceptions.ProblemException):
        cnx.add_error_handler(obj, exceptions.render_exception_message)

# Register code defined data structure from db_models
at_db = SQLAlchemy(cnx.app)
from . import db_models

# Register db migration toolings
at_migrate = Migrate(cnx.app, at_db, render_as_batch=True)

# Regsiter swagger.yaml as openapi endpoint
cnx.add_api('swagger.yaml', arguments={'title': 'AutoTrader'}, pythonic_params=True)

# Regsiter /api-docs as the swagger ui
flask_api_doc(cnx.app, config_path=SWAGGER_CONFIG, url_prefix=SWAGGER_URL_PREFIX)

# Backward compatible with Flask app
app = cnx.app