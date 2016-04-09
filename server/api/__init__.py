from flask_restplus import Api
from .requests import ns as requests_ns
from .comments import ns as comments_ns
from .movies import ns as movies_ns
from .tvshows import ns as tvshows_ns
from flask import Blueprint

blueprint = Blueprint('api', __name__)
api = Api(blueprint,
    title='Plex Requests API',
    validate=True
)

api.add_namespace(requests_ns)
api.add_namespace(comments_ns)
api.add_namespace(movies_ns)
api.add_namespace(tvshows_ns)
