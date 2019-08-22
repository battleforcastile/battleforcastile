import os

from battleforcastile.utils.generate_turn import generate_turn

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_generate_turn_works_as_it_should():
    turn_number = 1
    state = {
        'board': [[], []]
    }
    hero_username = 'hero_username'
    enemy_username = 'enemy_username'
    num_cards_in_hand_left = 5
    turn = generate_turn(turn_number, state, hero_username, enemy_username, num_cards_in_hand_left)

    assert turn == {
        'number': turn_number,
        'hero': hero_username,
        'enemy': enemy_username,
        'state': state,
        'num_cards_in_hand_left': num_cards_in_hand_left
    }
