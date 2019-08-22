import random
from typing import List

from battleforcastile.utils.select_card_by_name import select_card_by_name


def select_random_boss_power(cards_path: str, boss: dict, cost_available: int) -> (List[dict], dict):
    selected_power = {}
    instances_to_invoke = []
    powers_to_choose_from = []

    powers = boss['powers']

    for power in powers:
        if power['cost'] <= cost_available:
            powers_to_choose_from.append(power)

    if len(powers_to_choose_from) > 0:
        index = random.randrange(0, len(powers_to_choose_from))
        selected_power = powers_to_choose_from[index]

    if selected_power:
        invoked_card = select_card_by_name(cards_path, selected_power['invocation']['card_name'])

        if invoked_card:
            for instance in range(selected_power['invocation']['num_instances']):
                instances_to_invoke.append(invoked_card)
    return instances_to_invoke, selected_power
