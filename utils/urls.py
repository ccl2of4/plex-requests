base_url = '/api'

def set_base_url(api_base_url):
    global base_url
    base_url = api_base_url

def drop_url():
    return url('/drop_db')

def requests_url():
    return url('/requests')

def request_url(request_id):
    return '{0}/{1}'.format(requests_url(), request_id)

def comments_url(request_id):
    return '{0}/comments'.format(request_url(request_id))

def comment_url(request_id, comment_id):
    return '{0}/{1}'.format(comments_url(request_id), comment_id)

def url(endpoint):
    return '{0}{1}'.format(base_url, endpoint)
