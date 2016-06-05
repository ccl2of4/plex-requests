import os

config = {}

# If the app should run in DEBUG mode.
# DEBUG mode prints stack traces, etc. to the console, but is insecure,
# so it should be disabled for prod.
config['DEBUG']         = bool(os.environ.get('DEBUG', True))

config['PORT']          = int(os.environ.get('PORT', 5000))

# API key for themoviedb
config['TMDB_API_KEY']  = os.environ.get('TMDB_API_KEY', '')

# Static folder from where a web app can be served.
config['STATIC_FOLDER'] = os.environ.get('STATIC_FOLDER', '')

# Path to the sqlite database.
config['DB_PATH']       = os.environ.get('DB_PATH', 'requests.db')
