import json

import requests
from battleforcastile.constants import BATTLEFORCASTILE_BRAIN_URL


def get_enemy_turn(match_id: int, turn_number: int, enemy_username: str) -> (dict, int):
    url = f'{BATTLEFORCASTILE_BRAIN_URL}/matches/{match_id}/turns/{turn_number}/hero/{enemy_username}/'
    r = requests.get(url)

    if r.status_code == 200:
        resp = r.json()
        return json.loads(resp['state']), resp['num_cards_in_hand_left']
    return {}, 0