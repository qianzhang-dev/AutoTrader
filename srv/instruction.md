### VSCode Extensions Recommended
1. humao.rest-client
2. ms-python.python
3. ms-python.vscode-pylance

### Initialize Project
1. Download a Python 3.7, Python 3.8, or Python 3.9
2. Create a virtual environment by `python -m venv .venv`
3. Activate the virtual environment by `source .venv/bin/activate`
4. Install production requirement.txt `pip install -r requirements.txt`
5. Install development dependencies `pip install -r test-requirements.txt`
6. Defind `FLASK_APP` environment variable `export FLASK_APP='swagger_server'`
7. Initialize database `flask db init` and apply the latest database change `flask db upgrade`
8. Explore the database by downloading `dbeaver`, connect to `./swagger_server/example.sqlite`

### Create local database for testing
- Framework: flask-migrate
- Initialize project localtion: `export FLASK_APP='swagger_server'`
- Create a database: `flask db init`
- Every time we make a change:
   1. Create a migration: `flask db migrate -m '<migration commit message>'`
   2. Apply to database: `flask db upgrade`

### Start Project
- Start with Python command `python -m swagger_server`
- Alternatively, start with Flask CLI `export FLASK_APP='swagger_server'` and `flask run --port 3000`

### Debug Project
1. Set breakpoint in the .py file
2. Hit F5, as the server will spin up in port `3000`
3. http://localhost:3000/api-docs

### Regenerate API
```
java -jar ./swagger-codegen-cli-3.0.24.jar generate \
   -i ./AutoTrader/srv/openapi_definition/v1.2.0.yml \
   -l python-flask \
   -o ./AutoTrader/srv

./recover.ps1
./recover.sh
```

### External Resources
1. All tickers: https://datahub.io/core/nyse-other-listings
2. Quote API: https://iexcloud.io/docs/api