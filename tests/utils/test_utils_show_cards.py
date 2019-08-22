import os

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.show_cards import show_cards


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_show_cards_works_when_there_are_cards():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards_in_hand = select_all_files(path)

    output = show_cards(cards_in_hand)

    assert len(output) > 0
    assert '1)' not in output
    assert 'Cost' not in output
    assert output.count('\n') == len(cards_in_hand)


def test_if_show_cards_works_when_there_are_no_cards():
    cards_in_hand = []

    output = show_cards(cards_in_hand)

    assert len(output) == 0


def test_if_show_cards_works_when_indices_are_asked():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards_in_hand = select_all_files(path)

    output = show_cards(cards_in_hand, with_indices=True)

    assert len(output) > 0
    assert '1)' in output
    assert output.count('\n') == len(cards_in_hand)


def test_if_show_cards_works_when_cost_is_specified():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards_in_hand = select_all_files(path)

    output = show_cards(cards_in_hand, with_cost=True)

    assert len(output) > 0
    assert '1)' not in output
    assert 'Cost' in output
    assert output.count('\n') == len(cards_in_hand)
