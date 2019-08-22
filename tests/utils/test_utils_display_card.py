import os

from battleforcastile.utils.display_card import display_card
from tests.fixtures import unit_card_value_2, spell_card_value_minus_2_enemy_all

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_unit_card_is_displayed_properly_without_cost():
    card = unit_card_value_2

    name = card['meta']['name']
    value = card['stats']['current_value']

    assert f'[UNIT]' in display_card(card)
    assert f'{name}' in display_card(card)
    assert f'[Value: {value}]' in display_card(card)


def test_if_unit_card_is_displayed_properly_with_cost():
    card = unit_card_value_2

    name = card['meta']['name']
    value = card['stats']['current_value']
    cost = card['stats']['cost']

    assert f'[UNIT]' in display_card(card, with_cost=True)
    assert f'{name}' in display_card(card, with_cost=True)
    assert f'[Value: {value}]' in display_card(card, with_cost=True)
    assert f'Cost: {cost}' in display_card(card, with_cost=True)


def test_if_spell_card_is_displayed_properly_without_cost():
    card = spell_card_value_minus_2_enemy_all

    name = card['meta']['name']
    description = card['meta']['description']

    assert f'[SPELL]' in display_card(card)
    assert f'{name}' in display_card(card)
    assert f'[{description}]' in display_card(card)


def test_if_spell_card_is_displayed_properly_with_cost():
    card = spell_card_value_minus_2_enemy_all

    name = card['meta']['name']
    description = card['meta']['description']
    cost = card['stats']['cost']

    assert f'[SPELL]' in display_card(card)
    assert f'{name}' in display_card(card)
    assert f'[{description}]' in display_card(card)
    assert f'Cost: {cost}' in display_card(card, with_cost=True)
