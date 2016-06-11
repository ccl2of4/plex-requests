import os
import tempfile
from plex_requests_api.config import config
from plex_requests_api.model.database import db
from plex_requests_api import app
from .apiutils import Client

class TestAPI(object):
    '''Base class to be extended for api tests'''

    def setup_method(self, method):
        # Override configuration to use test database
        self.db_fd, config['DB_PATH'] = tempfile.mkstemp()

        # Initialize a client to make calls to API
        self.client = Client(app)

        # Initialize and delete all data from database
        with app.app_context():
            db.initialize()
            db.execute('DELETE FROM requests WHERE 1')
            db.commit()

    def teardown_method(self, method):
        os.close(self.db_fd)
        os.unlink(config['DB_PATH'])
