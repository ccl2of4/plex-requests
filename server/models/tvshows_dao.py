import tmdbsimple as tmdb
from urlresolver import resolve_img_url

class TVShowsDao(object):

    def search(self, query):
        search = tmdb.Search()
        response = search.tv(query=query)
        res = []
        for s in search.results:
            tv_show = {}
            tv_show['name'] = s.get('name')
            tv_show['date'] = s.get('first_air_date')
            tv_show['poster_path'] = resolve_img_url(s.get('poster_path'))
            tv_show['backdrop_path'] = resolve_img_url(s.get('backdrop_path'))
            tv_show['summary'] = s.get('overview')
            tv_show['type'] = 'tv_show'
            res.append(tv_show)
        return res

dao = TVShowsDao()
