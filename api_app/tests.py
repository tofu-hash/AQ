import requests

url = ' http://127.0.0.1:8000/api/v1/'


def method(method_name: str, params: dict = {}, post: bool = False) -> tuple:
    if post:
        res = requests.post(url + method_name, data=params)
    else:
        res = requests.get(url + method_name, data=params)
    return res.json(), res.status_code


print(method('accounts/register/', params={
    'username': 'text',
    'password': 'text'
}, post=True))
print(method('accounts/login/', params={
    'username': 'text',
    'password': 'text'
}, post=True))
