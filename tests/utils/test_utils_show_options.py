import os

from battleforcastile.utils.show_options import show_options
from battleforcastile.utils.select_random_cards_from_set import select_random_cards_from_set


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_show_options_behaves_as_it_should_when_user_selects_a_valid_card():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cost_available = 10

    cards_in_hand = select_random_cards_from_set(path, 2)
    card_to_play_next = show_options(cards_in_hand, cost_available, 1)

    assert card_to_play_next != {}


def test_if_show_options_behaves_as_it_should_when_user_chooses_to_do_nothing():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cost_available = 10
    cards_in_hand = select_random_cards_from_set(path, 2)
    card_to_play_next = show_options(cards_in_hand, cost_available, 0)

    assert card_to_play_next == {}


def test_if_show_options_behaves_as_it_should_when_user_selects_an_invalid_card():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cost_available = 10

    cards_in_hand = select_random_cards_from_set(path, 2)
    card_to_play_next = show_options(cards_in_hand, cost_available, 10)

    assert card_to_play_next == {}


def test_if_show_options_raises_issue_when_trying_to_select_a_card_with_a_too_high_cost():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cost_available = 0

    cards_in_hand = select_random_cards_from_set(path, 2)
    card_to_play_next = show_options(cards_in_hand, cost_available, 10)

    assert card_to_play_next == {}
