import requests

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL

def get_latest_non_started_match_created_by_username(username: str):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/?first_user_username={username}&started=false&finished=false&desc=true&only_first=true'
    return requests.get(url)