#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import jsonify
import tmdbsimple as tmdb
from urlresolver import resolve_img_url
from database import Database
import json

tmdb.API_KEY = 'a550478f541c18be96e8019858fb837f'
app = Flask(__name__, static_folder='web')
database = Database()

@app.route('/requests', methods=['get'])
def get_requests():
    return json.dumps(database.get_requests())

@app.route('/requests', methods=['delete'])
def delete_request():
    item = request.get_json()['item']
    database.delete_request(item)
    return ('', 204)

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
        res['movies'].append(movie)
    return jsonify(res)

@app.route('/movierequest', methods=['post'])
def add_movie():
    movie = request.get_json()['movie']
    database.add_movie(movie)
    return ('', 201)

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
        res['tv_shows'].append(tv_show)
    return jsonify(res)

@app.route('/tvrequest', methods=['post'])
def add_tv():
    tv_show = request.get_json()['tv_show']
    database.add_tv_show(tv_show)
    return ('', 201)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
