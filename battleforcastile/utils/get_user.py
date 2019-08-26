import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL

def get_user(token: str):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/account/'
    return requests.post(url, data=json.dumps({
        'token': token
    }))