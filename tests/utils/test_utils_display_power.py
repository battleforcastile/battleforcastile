import os

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.display_power import display_power


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_power_is_displayed_properly():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'bosses')
    boss = select_all_files(path)[0]
    power = boss['powers'][0]

    name = power['name']
    invocation_unit = power['invocation']['card_name']
    invocation_instances = power['invocation']['num_instances']

    cost = power['cost']

    assert display_power(power) == f'{name} (Invocation: {invocation_instances} {invocation_unit}) - Cost: {cost}'
