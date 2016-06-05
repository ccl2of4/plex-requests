import os
import tempfile
from ..config import config
from .. import app, init_db, drop_db
from .apiutils import Client

class TestAPI(object):
    '''Base class to be extended for api tests'''

    def setup_method(self, method):
        # Override configuration to use test database
        self.db_fd, config['DB_PATH'] = tempfile.mkstemp()

        # Initialize a client to make calls to API
        self.client = Client(app)

        # Initialize and delete all data from database
        init_db()
        drop_db()

    def teardown_method(self, method):
        os.close(self.db_fd)
        os.unlink(config['DB_PATH'])
