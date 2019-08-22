import os

from nose.tools import raises

from battleforcastile.utils.show_board import show_board
from battleforcastile.utils.select_random_cards_from_set import select_random_cards_from_set


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@raises(Exception)
def test_if_show_board_raises_exception_if_board_is_none():
    board = None

    r = show_board(board)


@raises(Exception)
def test_if_show_board_raises_exception_if_board_has_wrong_length():
    board = [[]]

    r = show_board(board)


def test_if_board_is_shown_properly_when_empty():
    board = [[], []]

    r = show_board(board)
    rows = r.split('\n')
    assert '(empty)' in rows[0]
    assert '-------' in rows[1]
    assert '(empty)' in rows[2]


def test_if_board_is_shown_properly_when_it_has_cards():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards = select_random_cards_from_set(path, 2)
    board = [cards, cards]

    r = show_board(board)
    rows = r.split('\n')
    assert cards[0]['meta']['name'] in rows[0]
    assert cards[1]['meta']['name']  in rows[1]
    assert '-------' in rows[2]
    assert cards[0]['meta']['name'] in rows[3]
    assert cards[1]['meta']['name'] in rows[4]
