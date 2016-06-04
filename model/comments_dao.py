from database import db
from werkzeug.exceptions import NotFound

@db.transactions
class CommentsDAO(object):

    def get_all(self, request_id):
        requests.check_exists(request_id)
        query = db.execute('SELECT * FROM comments where request_id=?', (request_id,))
        result_list = query.fetchall()
        return result_list

    def get(self, request_id, comment_id):
        requests.check_exists(request_id)
        query = db.execute('SELECT * FROM comments where request_id=? and comment_id=?', (request_id, comment_id))
        result = query.fetchone()
        if not result:
            raise NotFound('No comment exists for id ' + comment_id + ' under request with id ' + request_id)
        return result

    def create(self, request_id, comment):
        requests.check_exists(request_id)
        db.execute('INSERT INTO comments (request_id, content, date) VALUES (?,?,CURRENT_TIMESTAMP)', (request_id, comment['content']))

    def delete(self, request_id, comment_id):
        self.check_exists(request_id, comment_id)
        query = db.execute('DELETE FROM comments WHERE request_id=? AND comment_id=?', (request_id, comment_id))

    def check_exists(self, request_id, comment_id):
        return self.get(request_id, comment_id)

dao = CommentsDAO()

from .requests_dao import dao as requests
