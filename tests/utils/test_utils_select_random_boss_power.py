import os

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.select_random_boss_power import select_random_boss_power


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_enemy_power_is_successfully_randomly_selected():
    cards_path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    bosses_path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    boss = select_all_files(bosses_path)[0]

    cost_available = 9
    invoked_cards, power = select_random_boss_power(cards_path, boss, cost_available)

    assert invoked_cards is not []
    assert len(invoked_cards) > 0
    assert invoked_cards[0]['meta']['name'] != ''
    assert invoked_cards[0]['stats']['cost'] <= cost_available

    assert power != {}
    assert power['name'] != ''


def test_if_boss_power_is_only_selected_if_cost_allows_it():
    cards_path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    bosses_path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    boss = select_all_files(bosses_path)[0]

    cost_available = 0
    invoked_cards, power = select_random_boss_power(cards_path, boss, cost_available)
    assert invoked_cards == []
    assert power == {}

