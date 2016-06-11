from json import loads as load_json, dumps as dump_json

class Client(object):
    def __init__(self, flask_app):
        self._client = flask_app.test_client()

    def get(self, url, params=None):
        return Response(self._client.get(url, query_string=params))

    def post(self, url, json):
        return Response(self._client.post(url, data=dump_json(json), content_type='application/json'))

    def put(self, url, json):
        return Response(self._client.put(url, data=dump_json(json), content_type='application/json'))

    def delete(self, url):
        return Response(self._client.delete(url))

class Response(object):
    def __init__(self, flask_response):
        self._response = flask_response

    @property
    def status_code(self):
        return self._response.status_code

    @property
    def json(self):
        return load_json(self._response.data.decode('utf-8'))
