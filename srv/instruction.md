### Initialize Project
1. Download a Python 3.7, Python 3.8, or Python 3.9
2. Create a virtual environment by `python -m venv .venv`
3. Activate the virtual environment by `source .venv/bin/activate`
4. Install production requirement.txt `pip install -r requirements.txt`
5. Install development dependencies `pip install -r test-requirements.txt`
6. Defind `FLASK_APP` environment variable `export FLASK_APP='swagger_server'`
7. Initialize database `flask db init` and apply the latest database change `flask db upgrade`
8. Explore the database by downloading `dbeaver`, connect to `./swagger_server/example.sqlite`

### Start Project
- Start with Python command `python -m swagger_server`
- Alternatively, start with Flask CLI `export FLASK_APP='swagger_server'` and `flask run --port 3000`

### Create local database for testing
- Framework: flask-migrate
- Initialize project localtion: `export FLASK_APP='swagger_server'`
- Create a database: `flask db init`
- Every time we make a change:
   1. Create a migration: `flask db migrate -m '<migration commit message>'`
   2. Apply to database: `flask db upgrade`