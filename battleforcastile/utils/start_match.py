import json

import requests
from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL
from battleforcastile.exceptions import MatchCouldNotBeStartedException


def start_match(match_id: int):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/{match_id}/'
    r = requests.patch(url, data=json.dumps({
        'started': True
    }))

    if r.status_code != 200:
        raise MatchCouldNotBeStartedException()