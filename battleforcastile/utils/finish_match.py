import json

import requests
from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL


# TODO: Create unittest
def finish_match(match_id: int, winner_username: str = None):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/{match_id}/'
    return requests.patch(url, data=json.dumps({
        'id': match_id,
        'winner_username': winner_username,
        'finished': True
    }))