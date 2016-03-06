import tmdbsimple as tmdb
import requests

def resolve_img_url(url):
    if None == url:
        return None
    return 'https://image.tmdb.org/t/p/' + 'w92' + url
