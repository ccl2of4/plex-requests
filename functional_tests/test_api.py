import requests
from utils.urls import *
from utils.fixtures import *
from .config import config

class TestAPI(object):
    '''Base class to be extended for functional tests'''

    def setup_method(self, method):
        set_base_url(config['API_BASE_URL'])
        requests.delete(drop_url())

    @classmethod
    def teardown_class(cls):
        requests.delete(drop_url())
