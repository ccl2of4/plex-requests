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
        conn.execute('''CREATE TABLE IF NOT EXISTS requests
            (type text, name text, date text);''')

    def get_requests(self):
        conn = self.get_conn()
        query = conn.execute('SELECT * FROM requests')
        colname = [ d[0] for d in query.description ]
        result_list = [ dict(zip(colname, r)) for r in query.fetchall() ]
        return result_list

    def delete_request(self, request):
        conn = self.get_conn()
        conn.execute('DELETE FROM requests WHERE type=? and name=? and date=?', (request['type'], request['name'], request['date']))

    def add_movie(self, movie):
        conn = self.get_conn()
        conn.execute('INSERT INTO requests VALUES (?,?,?)', ('movie', movie['name'], movie['date']))

    def add_tv_show(self, tv_show):
        conn = self.get_conn()
        conn.execute('INSERT INTO requests VALUES (?,?,?)', ('tv_show', tv_show['name'], tv_show['date']))
