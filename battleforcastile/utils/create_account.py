import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL

def create_account(email: str, username: str, password: str):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/account/create/'
    return requests.post(url, data=json.dumps({
        'email': email,
        'username': username,
        'password': password
    }))