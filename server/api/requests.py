from flask_restplus import Namespace, Resource, fields
from flask import request as r
from model.requests_dao import dao
from .comments import comment

ns = Namespace('requests', description='Requests operations')

request = ns.model('Request', {
    'request_id': fields.String(readOnly=True, description="The id of the request"),
    'name': fields.String(required=True, description='The name of the request'),
    'date': fields.String(required=True, description='The release date of the request'),
    'type': fields.String(required=True, enum=['movie', 'tv_show'], description='Type of request'),
    'comments' : fields.List(fields.Nested(comment))
})

@ns.route('')
class Requests(Resource):

    @ns.marshal_list_with(request)
    def get(self):
        '''List all requests'''
        return dao.get_all()

    @ns.expect(request)
    @ns.response(201, 'Success')
    def post(self):
        '''Create a request'''
        dao.create(r.json)
        return ('', 201)

@ns.route('/<request_id>')
@ns.response(404, 'Request not found')
class Request(Resource):

    @ns.marshal_with(request)
    def get(self, request_id):
        '''Fetch a request by id'''
        return dao.get(request_id)

    @ns.response(204, 'Success')
    def delete(self, request_id):
        '''Delete a request by id'''
        dao.delete(request_id)
        return ('', 204)
