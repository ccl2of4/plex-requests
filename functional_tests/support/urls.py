from ..config import config

def requests_url():
    return url('/requests')

def request_url(request_id):
    return '{0}/{1}'.format(requests_url(), request_id)

def comments_url(request_id):
    return '{0}/comments'.format(request_url(request_id))

def comment_url(request_id, comment_id):
    return '{0}/{1}'.format(comments_url(request_id), comment_id)

def url(endpoint):
    base_url = config['API_BASE_URL']
    return '{0}{1}'.format(base_url, endpoint)
