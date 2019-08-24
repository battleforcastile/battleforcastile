import json

import requests
from battleforcastile.constants import BATTLEFORCASTILE_MATCH_RECORDER_URL


def search_match(username: str, character: dict):
    url = f'{BATTLEFORCASTILE_MATCH_RECORDER_URL}/matches/search/'
    return requests.post(url, data=json.dumps({'user': {
        'username': username,
        'character': character
    }}))