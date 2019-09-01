import os

from battleforcastile.cli.cards import CURRENT_PATH
from battleforcastile.constants import CARDS_FOLDER_NAME, MAX_NUM_CARDS_IN_HAND, MAX_NUM_TURNS, \
    HERO_BOARD_SIDE, ENEMY_BOARD_SIDE, CARDS_FOLDER_PATH
from battleforcastile.exceptions import HeroPlayerHasWonException
from battleforcastile.utils.calculate_current_value import calculate_current_value
from battleforcastile.utils.display_match_state import display_match_state
from battleforcastile.utils.get_new_state_after_enemy_turn import get_new_state_after_enemy_turn
from battleforcastile.utils.has_lost import has_lost
from battleforcastile.utils.play_hero_turn import play_hero_turn
from battleforcastile.utils.select_random_cards_from_set import select_random_cards_from_set
from battleforcastile.utils.send_turn import send_turn


def play_multiplayer_game(hero: dict = None,
                          enemy: dict = None,
                          should_start: bool = None,
                          match_id: int = None,
                          hero_username: str = None,
                          enemy_username: str = None,
                          e2e_mode: bool = False):

    core_set_path = os.path.join(CARDS_FOLDER_PATH, hero['meta']['class'])
    cards_in_hand = select_random_cards_from_set(core_set_path, MAX_NUM_CARDS_IN_HAND, e2e_mode=e2e_mode)

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
        if should_start:
            if len(cards_in_hand) > 0:
                display_match_state(f'HERO ({hero_username}) Turn Start ({turn_number} Cost Available)', state, hero,
                                    enemy)
                state, cards_in_hand= play_hero_turn(turn_number, state, cards_in_hand)

                state['hero']['value'] = calculate_current_value(state['board'][HERO_BOARD_SIDE])
                state['enemy']['value'] = calculate_current_value(state['board'][ENEMY_BOARD_SIDE])

            state = send_turn(match_id, turn_number, state, hero_username, enemy_username, len(cards_in_hand))

            # TODO: Create unittest
            state, num_cards_in_hand_left_from_enemy = get_new_state_after_enemy_turn(
                match_id, turn_number, enemy_username)

        else:
            # TODO: Create unittest
            state, num_cards_in_hand_left_from_enemy = get_new_state_after_enemy_turn(
                match_id, turn_number, enemy_username)

            if len(cards_in_hand) > 0:
                display_match_state(f'HERO ({hero_username}) Turn Start ({turn_number} Cost Available)', state, hero,
                                    enemy)
                state, cards_in_hand = play_hero_turn(turn_number, state, cards_in_hand)

                state['hero']['value'] = calculate_current_value(state['board'][HERO_BOARD_SIDE])
                state['enemy']['value'] = calculate_current_value(state['board'][ENEMY_BOARD_SIDE])

            state = send_turn(match_id, turn_number, state, hero_username, enemy_username, len(cards_in_hand))

        if has_lost(state['enemy']['value'], state['hero']['value'], len(cards_in_hand),
                    num_cards_in_hand_left_from_enemy):
            display_match_state(f'Final Board ({hero_username})', state, hero, enemy)
            raise HeroPlayerHasWonException()
