import os

from battleforcastile.utils.select_all_files import select_all_files

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_all_bosses_can_be_selected():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    bosses = select_all_files(path)
    assert len(bosses) == 1
    assert bosses[0]['meta']['name'] != ''
