import os
import plex_requests_api

dirname = os.path.dirname(plex_requests_api.__file__)

config = {}

# The location of the sqlite database, relative to plex_requests_api module.
# This database is wiped between every test. The server should be configured to
# use this same database
config['DB_PATH']       = os.path.join(dirname, os.environ.get('DB_PATH', 'test_requests.db'))

# The base url for the api. Used by the tests
config['API_BASE_URL']  = os.environ.get('API_BASE_URL', 'http://localhost:5000/api')
