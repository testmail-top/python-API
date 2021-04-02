"""
    Example of accessing the.test mail.top api in python
    To work, you need to fill in the data: YOU_TOKEN_API, YOU_EMAIL
"""

import requests


class API(object):

    def __init__(self, token: str, timeout=3):
        self.token = token
        self.timeout = timeout

    def check_mail(self, data, ip=None):
        params = {'data': data}
        if ip is not None:
            params['ip'] = ip
        response = None
        try:
            response = requests.get(url="https://api.testmail.top/domain/check", params=params, timeout=self.timeout,
                                    headers={'Authorization': 'Bearer {}'.format(self.token)})
        except TimeoutError as e:
            print(e)

        return response


if __name__ == '__main__':
    _token = 'YOU_TOKEN_API'
    _api = API(token=_token)
    request = _api.check_mail(data='YOU_EMAIL')
    print(request.status_code, request.text)
