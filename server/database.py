import sqlite3

class Database:

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __init__(self):
        self.create_db()

    def get_conn(self):
        conn = sqlite3.connect('requests.db')
        conn.execute('PRAGMA foreign_keys = ON;')
        conn.row_factory = Database.dict_factory
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
            foreign key (request_id) references requests(request_id) on delete cascade);''')

db = Database()
