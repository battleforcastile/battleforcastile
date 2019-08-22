import os

from battleforcastile.utils.select_all_files import select_all_files

from battleforcastile.utils.display_boss import display_boss

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_boss_is_displayed_properly():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    boss = select_all_files(path)[0]

    name = boss['meta']['name']
    level = boss['stats']['level']

    assert display_boss(boss) == f'{name} (Level: {level})'
