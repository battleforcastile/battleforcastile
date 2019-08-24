import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_AUTH_URL

def create_account(email: str, username: str, password: str):
    url = f'{BATTLEFORCASTILE_AUTH_URL}/users/'
    return requests.post(url, data=json.dumps({
        'email': email,
        'username': username,
        'password': password
    }))