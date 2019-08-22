import os

from battleforcastile.constants import ENEMY_BOARD_SIDE, HERO_BOARD_SIDE
from battleforcastile.utils.apply_action_to_board import apply_action_to_board
from tests.fixtures import unit_card_value_2, spell_card_value_minus_2_enemy_all, unit_card_value_3, \
    spell_card_value_plus_2_hero_highest, spell_card_value_minus_2_enemy_highest, spell_card_value_minus_2_enemy_lowest

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_playing_units_works_as_it_should():

    state = {
        'board': [[], []]
    }

    state = apply_action_to_board(state, unit_card_value_2, ENEMY_BOARD_SIDE)

    assert state['board'][ENEMY_BOARD_SIDE][0] == unit_card_value_2


def test_playing_spell_works_as_it_should_when_there_are_no_cards_on_the_board():

    state = {
        'board': [[], []]
    }

    state = apply_action_to_board(state, spell_card_value_minus_2_enemy_all, ENEMY_BOARD_SIDE)

    assert len(state['board'][ENEMY_BOARD_SIDE]) == 0
    assert len(state['board'][HERO_BOARD_SIDE]) == 0


def test_playing_spells_with_all_selection_works_as_it_should():

    state = {
        'board': [[unit_card_value_3], []]
    }

    state = apply_action_to_board(state, spell_card_value_minus_2_enemy_all, ENEMY_BOARD_SIDE)

    assert state['board'][ENEMY_BOARD_SIDE][0]['stats']['current_value'] == (
            unit_card_value_3['stats']['current_value'] + spell_card_value_minus_2_enemy_all['stats']['current_value'])


def test_if_playing_spells_with_all_selection_can_kill_a_unit():

    state = {
        'board': [[unit_card_value_2], []]
    }

    state = apply_action_to_board(state, spell_card_value_minus_2_enemy_all, ENEMY_BOARD_SIDE)

    assert len(state['board'][ENEMY_BOARD_SIDE]) == 0


def test_if_playing_spells_with_highest_selection_work_as_it_should():

    state = {
        'board': [[], [unit_card_value_2, unit_card_value_3]]
    }

    state = apply_action_to_board(state, spell_card_value_plus_2_hero_highest, HERO_BOARD_SIDE)

    assert state['board'][HERO_BOARD_SIDE][1]['stats']['current_value'] == (
            unit_card_value_3['stats']['current_value'] +
            spell_card_value_plus_2_hero_highest['stats']['current_value'])


def test_if_playing_spells_with_highest_selection_can_kill_a_unit():
    state = {
        'board': [[unit_card_value_2], []]
    }

    state = apply_action_to_board(state, spell_card_value_minus_2_enemy_highest, ENEMY_BOARD_SIDE)

    assert len(state['board'][ENEMY_BOARD_SIDE]) == 0


def test_if_playing_spells_with_lowest_selection_work_as_it_should():

    state = {
        'board': [[unit_card_value_3], []]
    }

    state = apply_action_to_board(state, spell_card_value_minus_2_enemy_lowest, ENEMY_BOARD_SIDE)

    assert state['board'][ENEMY_BOARD_SIDE][0]['stats']['current_value'] == (
            unit_card_value_3['stats']['current_value'] + spell_card_value_minus_2_enemy_lowest['stats']['current_value'])


def test_if_playing_spells_with_lowest_selection_can_kill_a_unit():
    state = {
        'board': [[unit_card_value_2, unit_card_value_3], []]
    }

    state = apply_action_to_board(state, spell_card_value_minus_2_enemy_lowest, ENEMY_BOARD_SIDE)

    # We check that "unit_card_1" has died
    assert state['board'][ENEMY_BOARD_SIDE][0]['stats']['current_value'] == unit_card_value_3['stats']['current_value']
