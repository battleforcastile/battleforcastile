import os

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.display_hero import display_hero


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_hero_is_displayed_properly():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'heroes')
    klass = select_all_files(path)[0]

    name = klass['meta']['name']
    level = klass['stats']['level']

    assert display_hero(klass) == f'{name} (Level: {level})'
