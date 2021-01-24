# pylint: disable=import-error

from os import path

import connexion

from swagger_server import encoder
from swagger_ui import flask_api_doc


SWAGGER_CONFIG = path.join(path.dirname(__file__), 'swagger', 'swagger.yaml')


def main():
    app_ = connexion.App(__name__, specification_dir='./swagger/')
    app_.app.json_encoder = encoder.JSONEncoder
    app_.add_api('swagger.yaml', arguments={'title': 'AutoTrader'}, pythonic_params=True)
    flask_api_doc(app_.app, config_path=SWAGGER_CONFIG, url_prefix='/api-docs')
    app_.run(port=3000)


if __name__ == '__main__':
    main()
