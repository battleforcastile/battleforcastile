def display_power(power: dict) -> str:
    name = power['name']
    invocation_unit = power['invocation']['card_name']
    invocation_instances = power['invocation']['num_instances']

    cost = power['cost']

    return f'{name} (Invocation: {invocation_instances} {invocation_unit}) - Cost: {cost}'
