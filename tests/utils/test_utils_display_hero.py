from battleforcastile.utils.display_hero import display_hero
from tests.fixtures import black_forest_elf


def test_if_hero_is_displayed_properly():
    hero = black_forest_elf

    name = hero['meta']['name']
    level = hero['stats']['level']

    assert display_hero(hero) == f'{name} (Level: {level})'
