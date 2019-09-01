from battleforcastile.utils.display_power import display_power
from tests.fixtures import black_angel


def test_if_power_is_displayed_properly():
    boss = black_angel
    power = boss['powers'][0]

    name = power['name']
    invocation_unit = power['invocation']['card_name']
    invocation_instances = power['invocation']['num_instances']

    cost = power['cost']

    assert display_power(power) == f'{name} (Invocation: {invocation_instances} {invocation_unit}) - Cost: {cost}'
