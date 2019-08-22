import click


def display_card(card: dict, with_cost: bool = False) -> str:
    name = card['meta']['name']
    type = card['meta']['type']
    description = card['meta'].get('description')

    value = card['stats']['current_value']
    cost = card['stats']['cost']

    output = ''
    if type == 'spell':
        output += click.style('[SPELL] ', fg='cyan', bold=True)
    elif type == 'unit':
        output += click.style('[UNIT] ', fg='cyan', bold=True)

    output += f'{name} '

    if type == 'spell':
        output += click.style(f'[{description}] ', fg='red', bold=True)
    elif type == 'unit':
        output += click.style(f'[Value: {value}] ', fg='red', bold=True)

    if with_cost:
        output += click.style(f'Cost: {cost}', fg='blue', bold=True)

    return output