import os

config = {}

# The base url for the api. Used by the tests
config['API_BASE_URL']  = os.environ.get('API_BASE_URL', 'http://localhost:5000/api')
