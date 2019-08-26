import json

import requests
from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL


def search_match(username: str, character: dict):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/search/'
    return requests.post(url, data=json.dumps({'user': {
        'username': username,
        'character': character
    }}))