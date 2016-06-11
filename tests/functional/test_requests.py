import requests
from plex_requests_api.model.database import db
from tests.utils.urls import *
from tests.utils.fixtures import *
from .config import config
from .test_api import TestAPI

class TestRequests(TestAPI):

    def test_create(self):
        r = requests.post(requests_url(), json=minimal_request())
        assert r.status_code == 201

    def test_get_all_empty(self):
        r = requests.get(requests_url())
        assert r.status_code == 200
        assert len(r.json()) == 0

    def test_get_all_after_create(self):
        self.test_create()
        r = requests.get(requests_url())
        assert r.status_code == 200
        assert len(r.json()) == 1

    def test_delete(self):
        self.test_create()
        r = requests.get(requests_url())
        request_id = r.json()[0]['request_id']
        r = requests.delete(request_url(request_id))
        assert r.status_code == 204
        self.test_get_all_empty()

    def test_delete_404(self):
        r = requests.delete(request_url('lol'))
        assert r.status_code == 404

    def test_get_after_create(self):
        self.test_create()
        r = requests.get(requests_url())
        request_id = r.json()[0]['request_id']
        r = requests.get(request_url(request_id))
        assert r.status_code == 200

    def test_get_404(self):
        r = requests.get(request_url('lol'))
        assert r.status_code == 404
