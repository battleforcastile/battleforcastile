import os

from battleforcastile.utils.has_lost import has_lost
from tests.fixtures import unit_card_value_2

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_has_lost_is_true_when_character_has_lower_value_and_an_empty_hand():
    state = {
        'hero': {
            'value': 10
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    cards_in_hand = []
    assert has_lost(state['hero']['value'], state['enemy']['value'], cards_in_hand) is True


def test_if_has_lost_is_false_when_character_has_lower_value_but_not_an_empty_hand():
    state = {
        'hero': {
            'value': 10
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    cards_in_hand = [unit_card_value_2]
    assert has_lost(state['hero']['value'], state['enemy']['value'], cards_in_hand) is False


def test_if_has_lost_is_false_when_character_has_bigger_value_and_an_empty_hand():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 10
        }
    }
    cards_in_hand = []
    assert has_lost(state['hero']['value'], state['enemy']['value'], cards_in_hand) is False


def test_if_has_lost_is_false_when_character_has_bigger_value_and_not_an_empty_hand():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 10
        }
    }
    cards_in_hand = [unit_card_value_2]
    assert has_lost(state['hero']['value'], state['enemy']['value'], cards_in_hand) is False


def test_if_has_lost_is_true_when_character_has_equal_value_an_empty_hand_and_wins_tie_false():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    cards_in_hand = []
    assert has_lost(state['hero']['value'], state['enemy']['value'], cards_in_hand, wins_tie=False) is True


def test_if_has_lost_is_false_when_character_has_equal_value_an_empty_hand_and_wins_tie_true():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    cards_in_hand = []
    assert has_lost(state['hero']['value'], state['enemy']['value'], cards_in_hand, wins_tie=True) is False
