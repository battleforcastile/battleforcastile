import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL

def create_match(username: str, character: dict):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/enqueue-match/'
    return requests.post(url, data=json.dumps({
        'first_user': {
            'username': username,
            'character': character
        }
    }))