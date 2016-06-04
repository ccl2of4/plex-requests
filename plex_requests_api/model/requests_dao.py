from .database import db
from werkzeug.exceptions import NotFound

@db.transactions
class RequestsDAO(object):

    def get_all(self, **kwargs):
        query = db.execute('SELECT * FROM requests')
        result_list = query.fetchall()
        return self._post_process(result_list, **kwargs)

    def get(self, request_id, **kwargs):
        query = db.execute('SELECT * FROM requests where request_id=?', (request_id,))
        result = query.fetchone()
        if not result:
            raise NotFound('No request exists for id ' + request_id)
        return self._post_process((result,), **kwargs)

    def create(self, request):
        db.execute('INSERT INTO requests (type, name, date) VALUES (?,?,?)', (request['type'], request['name'], request['date']))

    def delete(self, request_id):
        self.check_exists(request_id)
        query = db.execute('DELETE FROM requests WHERE request_id=?', (request_id,))

    def check_exists(self, request_id):
        return self.get(request_id)

    def _post_process(self, requests, nest_comments=False):
        if not nest_comments:
            return requests
        return [self._nest_comments(r) for r in requests]

    def _nest_comments(self, request):
        request['comments'] = comments.get_all(request['request_id'])
        return request

dao = RequestsDAO()

from .comments_dao import dao as comments
