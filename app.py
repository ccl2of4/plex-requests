#!/usr/bin/env python
import tmdbsimple as tmdb
from flask import Flask, send_file, redirect
from flask_restplus import Resource, Api
from api import blueprint as api

app = Flask(__name__, static_folder='../web', instance_relative_config=True)
app.config.from_pyfile('plex-requests.cfg')
app.register_blueprint(api, url_prefix='/api')
tmdb.API_KEY = app.config['API_KEY']

# GUI served at '/'

@app.route('/')
def index():
    return send_file('../web/index.html')

@app.route('/<path:path>')
def redirect_to_index(path):
    return redirect('/')

# Swagger GUI served at '/api'

@app.route('/api/<path:path>')
def api_index(path):
    return redirect('/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
