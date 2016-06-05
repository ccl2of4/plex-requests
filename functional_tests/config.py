import os

config = {}

# Path to the sqlite database. The database is wiped between every test.
# Note: using an in-memory database will not currently work because the sqlite
# connection is closed between every request
config['DB_PATH']       = os.environ.get('DB_PATH', 'test_requests.db')

# The base url for the api. Used by the tests
config['API_BASE_URL']  = os.environ.get('API_BASE_URL', 'http://localhost:5000/api')
