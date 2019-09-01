import os

from battleforcastile.utils.display_boss import display_boss
from tests.fixtures import black_angel


def test_if_boss_is_displayed_properly():
    boss = black_angel

    name = boss['meta']['name']
    level = boss['stats']['level']

    assert display_boss(boss) == f'{name} (Level: {level})'
