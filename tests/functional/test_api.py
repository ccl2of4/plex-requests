import requests
import sqlite3
import os
from tests.utils.urls import *
from tests.utils.fixtures import *
from .config import config

class TestAPI(object):
    '''Base class to be extended for functional tests'''

    @classmethod
    def setup_class(cls):
        set_base_url(config['API_BASE_URL'])

    def setup_method(self, method):
        self.drop_all()

    def teardown_method(self, method):
        self.drop_all()

    def drop_all(self):
        conn = sqlite3.connect(config['DB_PATH'])
        # Foreign keys enabled for cascade delete of all data
        conn.execute('PRAGMA foreign_keys = ON;')
        conn.execute('DELETE FROM requests WHERE 1')
        conn.commit()
