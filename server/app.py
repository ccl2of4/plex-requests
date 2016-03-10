#!/usr/bin/env python

from flask import url_for
from flask import redirect
from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
import tmdbsimple as tmdb
from urlresolver import resolve_img_url
from database import Database
import json

tmdb.API_KEY = 'a550478f541c18be96e8019858fb837f'
app = Flask(__name__, static_folder='../web')
database = Database()


# Web

@app.route('/', methods=['get'])
def index():
    return send_file('../web/views/index.html')

@app.route('/web/index.html', methods=['get'])
def old_index():
    return redirect(url_for('index'))


# Requests

@app.route('/requests', methods=['get'])
def get_requests():
    return json.dumps(database.get_requests())

@app.route('/requests', methods=['post'])
def add_request():
    item = request.get_json()['item']
    database.add_request(item)
    return ('', 201)

@app.route('/requests/<request_id>', methods=['delete'])
def delete_request(request_id):
    database.delete_request(request_id)
    return ('', 204)


# Comments

@app.route('/requests/<request_id>/comments', methods=['post'])
def add_comment(request_id):
    comment = request.get_json()['comment']
    database.add_comment(request_id, comment)
    return ('', 201)

@app.route('/requests/<request_id>/comments/<comment_id>', methods=['delete'])
def delete_comment(request_id, comment_id):
    database.delete_comment(request_id, comment_id)
    return ('', 204)


#Search

@app.route('/moviesearch', methods=['get'])
def search_movies():
    query = request.args.get('query')
    search = tmdb.Search()
    response = search.movie(query=query)
    res = {}
    res['movies'] = []
    for s in search.results:
        movie = {}
        movie['name'] = s.get('title')
        movie['date'] = s.get('release_date')
        movie['poster_path'] = resolve_img_url(s.get('poster_path'))
        movie['backdrop_path'] = resolve_img_url(s.get('backdrop_path'))
        movie['summary'] = s.get('overview')
        movie['type'] = 'movie'
        res['movies'].append(movie)
    return jsonify(res)

@app.route('/tvsearch', methods=['get'])
def search_tv():
    query = request.args.get('query')
    search = tmdb.Search()
    response = search.tv(query=query)
    res = {}
    res['tv_shows'] = []
    for s in search.results:
        tv_show = {}
        tv_show['name'] = s.get('name')
        tv_show['date'] = s.get('first_air_date')
        tv_show['poster_path'] = resolve_img_url(s.get('poster_path'))
        tv_show['backdrop_path'] = resolve_img_url(s.get('backdrop_path'))
        tv_show['summary'] = s.get('overview')
        tv_show['type'] = 'tv_show'
        res['tv_shows'].append(tv_show)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
