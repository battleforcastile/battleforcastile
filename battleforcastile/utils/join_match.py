import json

import requests
from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL


def join_match(username: str, character: dict):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/join/'
    return requests.post(url, data=json.dumps({'user': {
        'username': username,
        'character': character
    }}))