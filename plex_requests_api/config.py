import os

config = {}

config['DEBUG']         = bool(os.environ.get('DEBUG', True))
config['PORT']          = int(os.environ.get('PORT', 5000))
config['TMDB_API_KEY']  = os.environ.get('TMDB_API_KEY', '')
config['STATIC_FOLDER'] = os.environ.get('STATIC_FOLDER', '')
config['DB_PATH']       = os.environ.get('DB_PATH', 'requests.db')
config['API_BASE_URL']  = os.environ.get('API_BASE_URL', 'http://localhost:5000/api')
