import requests

from battleforcastile.constants import BATTLEFORCASTILE_MATCH_RECORDER_URL

def get_match_info(match_id: int) -> dict:
    url = f'{BATTLEFORCASTILE_MATCH_RECORDER_URL}/matches/{match_id}/'
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    return {}