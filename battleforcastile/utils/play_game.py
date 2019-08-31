import os

from battleforcastile.cli.cards import CURRENT_PATH
from battleforcastile.constants import CARDS_FOLDER_NAME, CORE_SET_FOLDER_NAME, MAX_NUM_CARDS_IN_HAND, MAX_NUM_TURNS, \
    HERO_BOARD_SIDE, ENEMY_BOARD_SIDE
from battleforcastile.utils.calculate_current_value import calculate_current_value
from battleforcastile.utils.display_match_state import display_match_state
from battleforcastile.utils.has_lost import has_lost
from battleforcastile.utils.play_enemy_turn import play_enemy_turn
from battleforcastile.utils.play_hero_turn import play_hero_turn
from battleforcastile.utils.select_random_cards_from_set import select_random_cards_from_set


def play_game(hero: dict = None, enemy: dict = None, e2e_mode: bool = False) -> bool:
    core_set_path = os.path.join(CURRENT_PATH, '..', CARDS_FOLDER_NAME, CORE_SET_FOLDER_NAME, hero['meta']['class'])
    did_hero_win = False

    cards_in_hand = select_random_cards_from_set(core_set_path, MAX_NUM_CARDS_IN_HAND, e2e_mode)

    state = {
        'hero': {
            'value': 0
        },
        'board': [[], []],
        'enemy': {
            'value': 0
        }
    }

    for turn_number in range(1, MAX_NUM_TURNS + 1):
        display_match_state(f'HERO Turn Start ({turn_number} Cost Available)', state, hero, enemy)
        state, cards_in_hand = play_hero_turn(turn_number, state, cards_in_hand)

        state = play_enemy_turn(core_set_path, turn_number, enemy, state, hero)

        state['hero']['value'] = calculate_current_value(state['board'][HERO_BOARD_SIDE])
        state['enemy']['value'] = calculate_current_value(state['board'][ENEMY_BOARD_SIDE])

        if has_lost(state['hero']['value'], state['enemy']['value'], len(cards_in_hand), len(cards_in_hand), wins_tie=True):
            break

        if has_lost(state['enemy']['value'], state['hero']['value'], len(cards_in_hand), len(cards_in_hand)):
            did_hero_win = True
            break

    return did_hero_win
