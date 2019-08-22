import os

from battleforcastile.utils.select_all_files import select_all_files

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_all_heroes_can_be_selected():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'heroes')
    heroes = select_all_files(path)
    assert len(heroes) == 1
    assert heroes[0]['meta']['name'] != ''
