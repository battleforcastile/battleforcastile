import time

import click

from battleforcastile.constants import HERO_BOARD_SIDE, ENEMY_BOARD_SIDE
from battleforcastile.utils.get_enemy_turn import get_enemy_turn
from battleforcastile.utils.get_match_info import get_match_info


# TODO: unittest
def get_new_state_after_enemy_turn(match_id: int, turn_number: int, enemy_username: str) -> (dict, int):
    click.echo('Please wait until your opponent finishes his/her turn/s...')
    state = {}
    num_cards_in_hand_left_from_enemy = 0
    while True:
        match = get_match_info(match_id)
        if match['finished']:
            break
        state, num_cards_in_hand_left_from_enemy = get_enemy_turn(match_id, turn_number, enemy_username)

        if state:
            state['hero']['value'], state['enemy']['value'] = (
                state['enemy']['value'], state['hero']['value'])
            state['board'][HERO_BOARD_SIDE], state['board'][ENEMY_BOARD_SIDE] = (
                state['board'][ENEMY_BOARD_SIDE], state['board'][HERO_BOARD_SIDE])
            break
        else:
            time.sleep(3)

    return state, num_cards_in_hand_left_from_enemy
