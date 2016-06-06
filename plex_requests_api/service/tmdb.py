import tmdbsimple
from ..config import config

tmdbsimple.API_KEY = config['TMDB_API_KEY']

class TMDBService(object):

    def search_movies(self, query):
        s = tmdbsimple.Search()

        try:
            s.movie(query=query)
        except Exception as e:
            self.handle_error(e)
            return []

        def transform(r):
            movie = {}
            movie['name'] = r.get('title')
            movie['date'] = r.get('release_date')
            movie['poster_path'] = resolve_img_url(r.get('poster_path'))
            movie['backdrop_path'] = resolve_img_url(r.get('backdrop_path'))
            movie['summary'] = r.get('overview')
            movie['type'] = 'movie'
            return movie

        return [transform(r) for r in s.results]

    def search_tv(self, query):
        s = tmdbsimple.Search()

        try:
            s.tv(query=query)
        except Exception as e:
            self.handle_error(e)
            return []

        def transform(s):
            tvshow = {}
            tvshow['name'] = s.get('name')
            tvshow['date'] = s.get('first_air_date')
            tvshow['poster_path'] = resolve_img_url(s.get('poster_path'))
            tvshow['backdrop_path'] = resolve_img_url(s.get('backdrop_path'))
            tvshow['summary'] = s.get('overview')
            tvshow['type'] = 'tv_show'
            return tvshow

        return [transform(r) for r in s.results]

    def handle_error(self, e):
        from .. import app
        app.logger.error('Error calling TMDB. {0}'.format(e))
        raise e

tmdb = TMDBService()
