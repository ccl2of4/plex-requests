import tmdbsimple as tmdb
from urlresolver import resolve_img_url

class MoviesDAO(object):

    def search(self, query):
        search = tmdb.Search()
        response = search.movie(query=query)
        res = []
        for s in search.results:
            movie = {}
            movie['name'] = s.get('title')
            movie['date'] = s.get('release_date')
            movie['poster_path'] = resolve_img_url(s.get('poster_path'))
            movie['backdrop_path'] = resolve_img_url(s.get('backdrop_path'))
            movie['summary'] = s.get('overview')
            movie['type'] = 'movie'
            res.append(movie)
        return res

dao = MoviesDAO()
