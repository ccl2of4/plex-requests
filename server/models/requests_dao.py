from database import db

class RequestsDAO(object):
    
    def get_all(self):
        conn = db.get_conn()
        query = conn.execute('SELECT * FROM requests')
        result_list = query.fetchall()
        for request in result_list:
            self._add_comments(request)
        return result_list

    def get(self, request_id):
        conn = db.get_conn()
        query = conn.execute('SELECT * FROM requests where request_id=?', (request_id,))
        result_list = query.fetchall()
        if not result_list:
            return None
        self._add_comments(request)
        return request

    def create(self, request):
        conn = db.get_conn()
        conn.execute('INSERT INTO requests (type, name, date) VALUES (?,?,?)', (request['type'], request['name'], request['date']))

    def delete(self, request_id):
        conn = db.get_conn()
        query = conn.execute('DELETE FROM requests WHERE request_id=?', (request_id,) )
        return query.rowcount != 0

    def _add_comments(self, request):
        conn = db.get_conn()
        query = conn.execute('SELECT * FROM comments where request_id=? ORDER BY date ASC', (str(request['request_id']),))
        comment_list = query.fetchall()
        request['comments'] = comment_list

dao = RequestsDAO()
