import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL

def login_user(username: str, password: str):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/account/login/'
    return requests.post(url, data=json.dumps({
        'username': username,
        'password': password
    }))