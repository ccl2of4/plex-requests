from utils.fixtures import *
from utils.urls import *
from .test_api import TestAPI

class TestComments(TestAPI):

    def setup_method(self, method):
        super().setup_method(method)

        r = self.client.post(requests_url(), json=minimal_request())
        r = self.client.get(requests_url())
        self.request_id = r.json[0]['request_id']

    def test_create(self):
        r = self.client.post(comments_url(self.request_id), json=minimal_comment())
        assert r.status_code == 201

    def test_get_all_empty(self):
        r = self.client.get(comments_url(self.request_id))
        assert r.status_code == 200
        assert len(r.json) == 0

    def test_get_all_after_create(self):
        self.test_create()
        r = self.client.get(comments_url(self.request_id))
        assert r.status_code == 200
        assert len(r.json) == 1

    def test_delete(self):
        self.test_create()
        r = self.client.get(comments_url(self.request_id))
        comment_id = r.json[0]['comment_id']
        r = self.client.delete(comment_url(self.request_id, comment_id))
        assert r.status_code == 204
        self.test_get_all_empty()

    def test_delete_404(self):
        r = self.client.delete(comment_url(self.request_id, 'lol'))
        assert r.status_code == 404

    def test_get_after_create(self):
        self.test_create()
        r = self.client.get(comments_url(self.request_id))
        comment_id = r.json[0]['comment_id']
        r = self.client.get(comment_url(self.request_id, comment_id))
        assert r.status_code == 200

    def test_get_404(self):
        r = self.client.get(comment_url(self.request_id, 'lol'))
        assert r.status_code == 404
