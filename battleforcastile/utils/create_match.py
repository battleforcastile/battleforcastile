import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_MATCH_RECORDER_URL

def create_match(username: str, character: dict):
    url = f'{BATTLEFORCASTILE_MATCH_RECORDER_URL}/matches/'
    return requests.post(url, data=json.dumps({'first_user': {
        'username': username,
        'character': character
    }}))