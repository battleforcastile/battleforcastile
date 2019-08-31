import json

import requests

from battleforcastile.exceptions import TurnCouldNotBeSentException
from battleforcastile.utils.generate_turn import generate_turn
from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL


def send_turn(match_id: int, turn_number: int, state: dict, hero_username: str,
              enemy_username: str, num_cards_in_hand_left: int) -> dict:
    turn = generate_turn(turn_number, state, hero_username, enemy_username, num_cards_in_hand_left)
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/{match_id}/turns/'
    r = requests.post(url, data=json.dumps(turn))

    if r.status_code == 201:
        return json.loads(r.json()['state'])
    else:
        raise TurnCouldNotBeSentException()