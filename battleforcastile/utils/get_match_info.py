import requests

from battleforcastile.constants import BATTLEFORCASTILE_BRAIN_URL

def get_match_info(match_id: int) -> dict:
    url = f'{BATTLEFORCASTILE_BRAIN_URL}/matches/{match_id}/'
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    return {}