import time

import click

from battleforcastile.constants import HERO_BOARD_SIDE, ENEMY_BOARD_SIDE
from battleforcastile.exceptions import EnemyPlayerConcededException, EnemyPlayerHasWonException, MatchNotFoundException
from battleforcastile.utils.get_enemy_turn import get_enemy_turn
from battleforcastile.utils.get_match_by_id import get_match_by_id


# TODO: unittest
def get_new_state_after_enemy_turn(match_id: int, turn_number: int, enemy_username: str) -> (dict, int):
    click.echo('Please wait until your opponent finishes his/her turn/s...')

    while True:
        r = get_match_by_id(match_id)
        if r.status_code == 200:
            match = r.json()
            if match['finished'] and match['winner_username']:
                raise EnemyPlayerHasWonException()

            if match['finished'] and not match['winner_username']:
                raise EnemyPlayerConcededException()
        else:
            raise MatchNotFoundException()

        state, num_cards_in_hand_left_from_enemy = get_enemy_turn(match_id, turn_number, enemy_username)

        if state:
            state['hero']['value'], state['enemy']['value'] = (
                state['enemy']['value'], state['hero']['value'])
            state['board'][HERO_BOARD_SIDE], state['board'][ENEMY_BOARD_SIDE] = (
                state['board'][ENEMY_BOARD_SIDE], state['board'][HERO_BOARD_SIDE])

            return state, num_cards_in_hand_left_from_enemy
        else:
            time.sleep(3)
