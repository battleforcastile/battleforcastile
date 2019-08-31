import requests

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL

def get_match_by_id(match_id: int):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/{match_id}/'
    return requests.get(url)