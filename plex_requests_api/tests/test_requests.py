from types import MethodType
from json import dumps, loads
from ..model.database import db
from ..config import config
from .. import app

client = None

def minimal_request():
    return {'name': 'some request', 'date': '10/26/2014', 'type': 'tv_show'}

def minimal_comment():
    return {'content': 'i am a comment'}

def setup_function(function):
    db._conn.executescript('DELETE FROM requests WHERE 1')

    global client
    app.config['TESTING'] = True
    client = app.test_client()

def post_json(client, url, json):
    return client.post(url, data=dumps(json), content_type='application/json')

def json(r):
    return loads(r.data.decode('utf-8'))

def test_create():
    r = post_json(client, '/api/requests', minimal_request())
    assert r.status_code == 201

def test_get_all_empty():
    r = client.get('/api/requests')
    assert r.status_code == 200
    assert len(json(r)) == 0

def test_get_all_after_create():
    test_create()
    r = client.get('/api/requests')
    assert r.status_code == 200
    assert len(json(r)) == 1
