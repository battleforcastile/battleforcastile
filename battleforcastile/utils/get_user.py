import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_AUTH_URL

def get_user(token: str):
    url = f'{BATTLEFORCASTILE_AUTH_URL}/get_user/'
    return requests.post(url, data=json.dumps({
        'token': token
    }))