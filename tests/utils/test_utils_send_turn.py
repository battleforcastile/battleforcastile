import json
from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL
from battleforcastile.utils.send_turn import send_turn
from battleforcastile.utils.generate_turn import generate_turn


@patch('battleforcastile.utils.send_turn.requests.post')
def test_if_send_turn_works_as_it_should(mocked_post):
    mocked_post.return_value.status_code = 201
    mocked_post.return_value.json.return_value = {
        'state': '{}'
    }
    hero_username = 'hero_username'
    enemy_username = 'enemy_username'

    match_id = 1
    turn_number = 1
    expected_state = {
        'board': [[], []]
    }
    num_cards_in_hand_left = 5

    send_turn(
        match_id, turn_number, expected_state, hero_username,
        enemy_username, num_cards_in_hand_left)

    mocked_post.assert_called_with(f'{BATTLEFORCASTILE_BACKEND_URL}/matches/{match_id}/turns/',
                                   data=json.dumps(
                                       generate_turn(turn_number, expected_state, hero_username,
                                                     enemy_username, num_cards_in_hand_left)))
