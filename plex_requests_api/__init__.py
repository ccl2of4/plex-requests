import tmdbsimple as tmdb
from flask import Flask, Blueprint, send_file, redirect
from flask_restplus import Resource, Api
from .config import config
from .resources.requests import ns as requests_ns
from .resources.comments import ns as comments_ns
from .resources.movies import ns as movies_ns
from .resources.tvshows import ns as tvshows_ns

app = Flask(__name__,
    static_url_path = '',
    static_folder   = config['STATIC_FOLDER'])

blueprint = Blueprint('api', __name__)
api = Api(blueprint,
    title    = 'Plex Requests API',
    validate = True)

api.add_namespace(requests_ns)
api.add_namespace(comments_ns)
api.add_namespace(movies_ns)
api.add_namespace(tvshows_ns)

app.register_blueprint(blueprint, url_prefix='/api')

tmdb.API_KEY = config['TMDB_API_KEY']

@app.route('/')
def index():
    return redirect('/index.html')

def run():
    app.run(
        host     = '0.0.0.0',
        port     = config['PORT'],
        debug    = config['DEBUG'],
        threaded = True)
