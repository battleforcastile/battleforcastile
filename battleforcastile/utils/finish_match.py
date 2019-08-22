import json

import requests
from battleforcastile.constants import BATTLEFORCASTILE_BRAIN_URL


def finish_match(match_id: int, winner_username: str = None):
    url = f'{BATTLEFORCASTILE_BRAIN_URL}/matches/{match_id}/'
    return requests.patch(url, data=json.dumps({
        'id': match_id,
        'winner': winner_username,
        'finished': True
    }))