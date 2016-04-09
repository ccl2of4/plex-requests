from database import db
from werkzeug.exceptions import NotFound

class CommentsDAO(object):

    def get_all(self, request_id):
        conn = db.get_conn()
        query = conn.execute('SELECT * FROM comments where request_id=?', (request_id,))
        result_list = query.fetchall()
        return result_list

    def get(self, request_id, comment_id):
        conn = db.get_conn()
        query = conn.execute('SELECT * FROM comments where request_id=? and comment_id=?', (request_id, comment_id))
        result_list = query.fetchall()
        if not result_list:
            raise NotFound()
        return result_list[0]

    def create(self, request_id, comment):
        conn = db.get_conn()
        conn.execute('INSERT INTO comments (request_id, content, date) VALUES (?,?,CURRENT_TIMESTAMP)', (request_id, comment['content']))

    def delete(self, request_id, comment_id):
        conn = db.get_conn()
        query = conn.execute('DELETE FROM comments WHERE request_id=? AND comment_id=?', (request_id, comment_id))
        if query.rowcount == 0:
            raise NotFound()

dao = CommentsDAO()
