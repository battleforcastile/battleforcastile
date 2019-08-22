import click

from battleforcastile.utils.display_match_state import display_match_state
from battleforcastile.utils.play_instances_from_enemy import play_instances_from_enemy
from battleforcastile.utils.select_random_boss_power import select_random_boss_power
from battleforcastile.utils.display_power import display_power


def play_enemy_turn(cards_path: str, turn_number: int, enemy: dict, state: dict, hero: dict) -> dict:
    display_match_state(f'ENEMY Turn Start ({turn_number} Cost Available)', state, hero, enemy)
    instances_to_invoke, power = select_random_boss_power(cards_path, enemy, turn_number)
    if instances_to_invoke:
        state['board'] = play_instances_from_enemy(state['board'], instances_to_invoke)
        click.echo(click.style(f'ACTION THIS TURN: ', fg='blue') + f' {display_power(power)}')
    else:
        click.echo(click.style(f'ACTION THIS TURN: ', fg='blue') + f'-')

    return state
