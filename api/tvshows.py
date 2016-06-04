from flask_restplus import Namespace, Resource, fields
from flask import request as r
from werkzeug.exceptions import BadRequest
from model.tvshows_dao import dao

ns = Namespace('tvshows', description='TV show searches')

tvshow = ns.model('TVShow', {
    'name': fields.String(requried=True, description="The name of the TV show"),
    'date': fields.String(required=True, description="The date of the TV show"),
    'poster_path': fields.String(description='Link to poster image for TV show'),
    'backdrop_path': fields.String(description='Link to backdrop image for TV show'),
    'summary': fields.String(description='Summary of TV show'),
    'type': fields.String(required=True, enum=['tv_show'], description='Type of request this is')
})

@ns.route('')
class TVShows(Resource):

    @ns.marshal_list_with(tvshow)
    @ns.param('query', _in='query', required=True)
    @ns.response(400, 'Missing query string')
    def get(self):
        '''Search TV shows'''
        query = r.args.get('query')
        if not query:
            raise BadRequest()
        return dao.search(query)
