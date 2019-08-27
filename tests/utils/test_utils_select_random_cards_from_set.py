import os

from nose.tools import raises

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.select_random_cards_from_set import select_random_cards_from_set

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_random_cards_from_set_can_be_selected():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards = select_random_cards_from_set(path, 1)
    assert len(cards) == 1
    assert cards[0]['meta']['name'] != ''


@raises(Exception)
def test_if_random_cards_from_set_return_none_if_set_has_fewer_cards_than_required():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    select_random_cards_from_set(path, 1000)


def test_if_random_cards_from_set_get_e2e_cards_when_e2e_mode_is_provided():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards = select_random_cards_from_set(path, 1, e2e_mode=True)
    for card in cards:
        assert card in select_all_files(f'{CURRENT_PATH}/../../tests/e2e/cards')
