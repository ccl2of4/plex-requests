import sqlite3
import threading
from ..config import config

class Database(object):

    def __init__(self, db_path):
        self._db_path = db_path
        self._threadlocal = threading.local()
        self._init_tables()

    def transactions(self, cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, self.transaction(getattr(cls, attr)))
        return cls

    def transaction(self, func):
        def error_decorator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self._transaction_level = 0
                self._conn.rollback()
                raise e
        def transaction_decorator(*args, **kwargs):
            self._transaction_level += 1
            retval = error_decorator(*args, **kwargs)
            self._transaction_level -= 1
            if (0 == self._transaction_level):
                self._conn.commit()
            return retval

        return transaction_decorator

    def execute(self, *args, **kwargs):
        return self._conn.execute(*args, **kwargs)

    def _init_tables(self):
        self._conn.executescript('''
            CREATE TABLE IF NOT EXISTS requests (
            request_id integer primary key,
            type text,
            name text,
            date text );

            CREATE TABLE IF NOT EXISTS comments (
            comment_id integer primary key,
            request_id integer,
            content text,
            date integer,
            foreign key (request_id) references requests(request_id) on delete cascade);
            ''')

    @property
    def _conn(self):
        if not self._threadinfo.conn:
            conn = sqlite3.connect(self._db_path)
            conn.execute('PRAGMA foreign_keys = ON;')
            conn.row_factory = Database._dict_factory
            self._threadinfo.conn = conn
        return self._threadinfo.conn

    @property
    def _transaction_level(self):
        return self._threadinfo.transaction_level

    @_transaction_level.setter
    def _transaction_level(self, value):
        self._threadinfo.transaction_level = value

    @property
    def _threadinfo(self):
        if not hasattr(self._threadlocal, 'threadinfo'):
            self._threadlocal.threadinfo = Database.ThreadInfo()
        return self._threadlocal.threadinfo

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    class ThreadInfo(object):
        def __init__(self):
            self.conn = None
            self.transaction_level = 0

db = Database(config['DB_PATH'])
