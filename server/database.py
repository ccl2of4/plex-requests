import sqlite3

class Database:

    def __init__(self):
        self.create_db()

    def get_conn(self):
        conn = sqlite3.connect('requests.db')
        conn.isolation_level = None
        return conn

    def create_db(self):
        conn = self.get_conn()
        conn.execute('''CREATE TABLE IF NOT EXISTS requests (
            request_id integer primary key,
            type text,
            name text,
            date text );''')
        conn.execute('''CREATE TABLE IF NOT EXISTS comments (
            comment_id integer primary key,
            request_id integer,
            content text,
            date integer,
            foreign key (request_id) references request(request_id) on delete cascade);''')

    def get_requests(self):
        conn = self.get_conn()
        query = conn.execute('SELECT * FROM requests')
        colname = [ d[0] for d in query.description ]
        result_list = [ dict(zip(colname, r)) for r in query.fetchall() ]
        for request in result_list:
            query = conn.execute('SELECT * FROM comments where request_id=? ORDER BY date ASC', str(request['request_id']))
            colname = [ d[0] for d in query.description ]
            comment_list = [ dict(zip(colname, r)) for r in query.fetchall() ]
            request['comments'] = comment_list
        return result_list

    def delete_request(self, request_id):
        conn = self.get_conn()
        conn.execute('DELETE FROM requests WHERE request_id=?', request_id )
        conn.execute('DELETE FROM comments WHERE request_id=?', request_id )

    def add_request(self, item):
        conn = self.get_conn()
        conn.execute('INSERT INTO requests (type, name, date) VALUES (?,?,?)', (item['type'], item['name'], item['date']))

    def add_comment(self, request_id, comment):
        conn = self.get_conn()
        conn.execute('INSERT INTO comments (request_id, content, date) VALUES (?,?,CURRENT_TIMESTAMP)', (request_id, comment['content']))

    def delete_comment(self, request_id, comment_id):
        print(request_id, comment_id)
        conn = self.get_conn()
        conn.execute('DELETE FROM comments WHERE request_id=? AND comment_id=?', (request_id, comment_id))
