from flask_restplus import Namespace, Resource, fields
from flask import request as r
from models.movies_dao import dao

ns = Namespace('movies', description='Movie searches')

movie = ns.model('Movie', {
    'name': fields.String(requried=True, description="The name of the movie"),
    'date': fields.String(required=True, description="The date of the movie"),
    'poster_path': fields.String(description='Link to poster image for movie'),
    'backdrop_path': fields.String(description='Link to backdrop image for movie'),
    'summary': fields.String(description='Summary of movie'),
    'type': fields.String(required=True, enum=['movie'], description='Type of request this is')
})

@ns.route('')
class Movies(Resource):

    @ns.marshal_list_with(movie, code=200)
    @ns.param('query', _in='query')
    @ns.response(400, 'Missing query string')
    def get(self):
        '''Search movies'''
        query = r.args.get('query')
        return dao.search(query) if query else ns.abort(400)
