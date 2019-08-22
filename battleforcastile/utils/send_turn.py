import json

import requests

from battleforcastile.utils.generate_turn import generate_turn


def send_turn(match_id: int, turn_number: int, state: dict, hero_username: str,
              enemy_username: str, num_cards_in_hand_left: int, BATTLEFORCASTILE_BRAIN_URL=None) -> dict:
    turn = generate_turn(turn_number, state, hero_username, enemy_username, num_cards_in_hand_left)
    url = f'{BATTLEFORCASTILE_BRAIN_URL}/matches/{match_id}/turns/'
    r = requests.post(url, data=json.dumps(turn))

    if r.status_code == 201:
        return json.loads(r.json()['state'])
    return {}