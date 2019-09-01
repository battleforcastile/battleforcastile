from battleforcastile.utils.show_cards import show_cards
from tests.fixtures import unit_card_value_1, unit_card_value_2


def test_if_show_cards_works_when_there_are_cards():
    cards_in_hand = [unit_card_value_1, unit_card_value_2]

    output = show_cards(cards_in_hand)

    assert len(output) > 0
    assert '1)' not in output
    assert 'Cost' not in output
    assert output.count('\n') == len(cards_in_hand)


def test_if_show_cards_works_when_there_are_no_cards():
    cards_in_hand = []

    output = show_cards(cards_in_hand)

    assert len(output) == 0


def test_if_show_cards_works_when_indices_are_asked():
    cards_in_hand = [unit_card_value_1, unit_card_value_2]

    output = show_cards(cards_in_hand, with_indices=True)

    assert len(output) > 0
    assert '1)' in output
    assert output.count('\n') == len(cards_in_hand)


def test_if_show_cards_works_when_cost_is_specified():
    cards_in_hand = [unit_card_value_1, unit_card_value_2]

    output = show_cards(cards_in_hand, with_cost=True)

    assert len(output) > 0
    assert '1)' not in output
    assert 'Cost' in output
    assert output.count('\n') == len(cards_in_hand)
