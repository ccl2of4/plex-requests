import requests
from plex_requests_api.model.database import db
from .support.urls import *
from .support.fixtures import *

request_id = ''

def setup_function(function):
    drop_all()

    global request_id
    r = requests.post(requests_url(), json=minimal_request())
    r = requests.get(requests_url())
    request_id = r.json()[0]['request_id']

@db.transaction
def drop_all():
    db._conn.execute('DELETE FROM requests WHERE 1')

def test_create():
    r = requests.post(comments_url(request_id), json=minimal_comment())
    assert r.status_code == 201

def test_get_all_empty():
    r = requests.get(comments_url(request_id))
    assert r.status_code == 200
    assert len(r.json()) == 0

def test_get_all_after_create():
    test_create()
    r = requests.get(comments_url(request_id))
    assert r.status_code == 200
    assert len(r.json()) == 1

def test_delete():
    test_create()
    r = requests.get(comments_url(request_id))
    comment_id = r.json()[0]['comment_id']
    r = requests.delete(comment_url(request_id, comment_id))
    assert r.status_code == 204
    test_get_all_empty()

def test_delete_404():
    r = requests.delete(comment_url(request_id, 'lol'))
    assert r.status_code == 404

def test_get_after_create():
    test_create()
    r = requests.get(comments_url(request_id))
    comment_id = r.json()[0]['comment_id']
    r = requests.get(comment_url(request_id, comment_id))
    assert r.status_code == 200

def test_get_404():
    r = requests.get(comment_url(request_id, 'lol'))
    assert r.status_code == 404
