import sqlite3
from flask import g
from ..config import config

class Database(object):

    def initialize(self):
        with open(config['SCHEMA_PATH']) as schema_file:
            schema = schema_file.read()
            self.executescript(schema)

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

    def executescript(self, *args, **kwargs):
        return self._conn.executescript(*args, **kwargs)

    def commit(self):
        return self._conn.commit()

    @property
    def _conn(self):
        conn = getattr(g, '_conn', None)
        if conn is None:
            conn = sqlite3.connect(config['DB_PATH'])
            conn.execute('PRAGMA foreign_keys = ON;')
            conn.row_factory = Database._dict_factory
            g._conn = conn
        return conn

    @property
    def _transaction_level(self):
        transaction_level = getattr(g, '_transaction_level', None)
        if transaction_level is None:
            transaction_level = g._transaction_level = 0
        return transaction_level

    @_transaction_level.setter
    def _transaction_level(self, value):
        g.transaction_level = value

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

db = Database()
