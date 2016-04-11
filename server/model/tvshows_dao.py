import tmdbsimple as tmdb
from werkzeug.exceptions import BadRequest
from .urlresolver import resolve_img_url

class TVShowsDAO(object):

    def search(self, query):
        s = tmdb.Search()
        s.tv(query=query)

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

dao = TVShowsDAO()
