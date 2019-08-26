import json
import os
from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL
from battleforcastile.utils.get_enemy_turn import get_enemy_turn

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@patch('battleforcastile.utils.get_enemy_turn.requests.get')
def test_if_get_enemy_turn_works_as_it_should(mocked_get):
    match_id = 1
    turn_number = 1
    hero_username = 'hero_username'
    enemy_username = 'enemy_username'
    num_cards_in_hand_left = 5

    expected_turn = {
        'turn_number': turn_number,
        'hero': hero_username,
        'enemy': enemy_username,
        'state': json.dumps({
            'hero': {
                'value': 10
            },
            'board': [[], []],
            'enemy': {
                'value': 20
            }
        }),
        'num_cards_in_hand_left': num_cards_in_hand_left
    }
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = expected_turn


    state, num_cards = get_enemy_turn(match_id, turn_number, enemy_username)

    assert state == json.loads(expected_turn['state'])
    assert num_cards == num_cards_in_hand_left

    url = f'{BATTLEFORCASTILE_BACKEND_URL}/matches/{match_id}/turns/{turn_number}/hero/{enemy_username}/'

    mocked_get.assert_called_with(url)
