import os

config = {}

# The location of the sqlite database. This database is wiped between every test.
# The server should be configured to use this same database
config['DB_PATH']       = os.environ.get('DB_PATH', 'test_requests.db')

# The base url for the api. Used by the tests
config['API_BASE_URL']  = os.environ.get('API_BASE_URL', 'http://localhost:5000/api')
