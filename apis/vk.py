import requests


class VKAPI:
    ENDPOINT = 'https://api.vk.com/method/'

    def __init__(self, client_id=None, v=5.103):
        self.v = v
        self.client_id = client_id

    def request(self, req_method, method, **params):
        params['v'] = self.v
        print(params)
        r = requests.request(req_method, VKAPI.ENDPOINT + method, params=params)
        print(r.text)
        return r.json()['response']

    def get(self, *args, **kwargs):
        return self.request('get', *args, **kwargs)

    def get_newsfeed(self, filters, count=1, **kwargs):
        return self.get('newsfeed.get',
                        filters=filters,
                        count=count,
                        **kwargs)

    def get_user(self, user_id, fields='', name_case=None, **kwargs):
        return self.get('users.get',
                        user_ids=user_id,
                        fields=fields,
                        name_case=name_case,
                        **kwargs)[0]