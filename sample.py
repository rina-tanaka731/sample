import requests

# api_url = 'https://rina731.backlog.com/api/v2/users/myself?apiKey=NNZoFfJWBmtyPX83LT3dZ8lVsKxMPjFxRAI7j9xPaex1IArjB9dscbbtsKQfSMt0'
# auth_request = 'https://rina731.backlog.com/OAuth2AccessRequest.action'
#
# utl_items = 'https://rina731.backlog.com/api/v2/space '
#
# item_data = {
#     'redirect_uri': 'https://rina731.backlog.com/v1/oauth2/callback',
#     'client_id': 'iH9pxHnUaHKXmgt70mfTDf44kMLV4HJu',
#     'response_type': 'code',
# }

BACKLOG_API_KEY = 'NNZoFfJWBmtyPX83LT3dZ8lVsKxMPjFxRAI7j9xPaex1IArjB9dscbbtsKQfSMt0'
BACKLOG_HOST = 'https://rina731.backlog.com'


def main():
    params = {'apiKey': BACKLOG_API_KEY}
    r = requests.get(BACKLOG_HOST + '/api/v2/users', params=params)
    print(r.status_code)
    print(r.headers)
    print(r.json())

# a_get = requests.get(auth_request, json=item_data)
# r_get = requests.get(api_url)
# item_get = requests.get(utl_items)


print(main())

# print(a_get.status_code)
# print(a_get.headers)
#
# print(item_get.status_code)
# print(item_get.headers)
#
# print(r_get.status_code)
# print(r_get.headers)
# print(r_get.json())