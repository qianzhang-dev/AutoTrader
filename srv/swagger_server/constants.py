from os import path

SWAGGER_SPEC_DIR = path.join(path.dirname(__file__), 'swagger')
SWAGGER_CONFIG = path.join(path.dirname(__file__), 'swagger', 'swagger.yaml')
SWAGGER_URL_PREFIX = '/api-docs'

SQLITE_DB_CONNSTR = 'sqlite:///example.sqlite'
