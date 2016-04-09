from flask_restplus import Namespace, Resource, fields
from flask import request as r
from models.comments_dao import dao

ns = Namespace('requests/<request_id>/comments', description='Comments operations')

comment = ns.model('Comment', {
    'comment_id': fields.String(readOnly=True, description="The id of the comment"),
    'request_id': fields.String(readOnly=True, description="The id of the associated request"),
    'date': fields.String(readOnly=True, description='The date the comment was added'),
    'content': fields.String(required=True, description='The content of the comment'),
})

@ns.route('')
class CommentList(Resource):

    @ns.marshal_list_with(comment)
    def get(self, request_id):
        '''List all comments'''
        return dao.get_all(request_id)

    @ns.expect(comment)
    @ns.response(204, 'Success')
    def post(self, request_id):
        '''Create a comment'''
        dao.create(request_id, r.json)
        return ('', 201)

@ns.route('/<comment_id>')
@ns.response(404, 'Comment not found')
class Comment(Resource):

    @ns.marshal_with(comment)
    def get(self, request_id, comment_id):
        '''Fetch a comment by id'''
        comment = dao.get(request_id, comment_id)
        return comment if comment else ns.abort(404)

    @ns.response(204, 'Success')
    def delete(self, request_id, comment_id):
        '''Delete a comment by id'''
        return ('', 204) if dao.delete(request_id, comment_id) else ns.abort(404)
