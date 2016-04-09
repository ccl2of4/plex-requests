import tmdbsimple as tmdb
from .urlresolver import resolve_img_url

class MoviesDAO(object):

    def search(self, query):
        s = tmdb.Search()
        s.movie(query=query)

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

dao = MoviesDAO()
