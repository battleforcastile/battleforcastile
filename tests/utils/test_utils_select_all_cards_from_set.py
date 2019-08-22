import os

from battleforcastile.utils.select_all_files import select_all_files


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_all_cards_from_set_can_be_selected():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards = select_all_files(path)
    assert len(cards) == 2
    assert cards[0]['meta']['name'] != ''
