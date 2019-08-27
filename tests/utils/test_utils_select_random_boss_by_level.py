import os

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.select_random_boss_by_level import select_random_boss_by_level

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_boss_is_randomly_selected_by_level():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    boss = select_random_boss_by_level(path, level=1)
    assert boss is not None


def test_if_boss_is_not_returned_if_level_is_unknown():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    boss = select_random_boss_by_level(path, level=100)
    assert boss is None

def test_if_e2e_boss_is_not_returned_when_e2e_mode_is_provided():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    boss = select_random_boss_by_level(path, level=1, e2e_mode=True)
    assert boss == select_all_files(f'{CURRENT_PATH}/../../tests/e2e/bosses')[0]