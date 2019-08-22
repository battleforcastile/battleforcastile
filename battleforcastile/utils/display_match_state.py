import click

from battleforcastile.utils.show_board import show_board
from battleforcastile.utils.display_boss import display_boss
from battleforcastile.utils.display_hero import display_hero


def display_match_state(title: str, state: dict, hero: dict, enemy: dict):
    # TODO: unittest
    click.echo(click.style('============================================================', fg='green', bold=True))
    click.echo(click.style(f'{title}', fg='green', bold=True))
    click.echo(click.style('============================================================', fg='green', bold=True))
    click.echo(click.style(f'ENEMY VALUE: ', fg='blue') + f'{state["enemy"]["value"]}')
    click.echo(click.style(f'ENEMY:', fg='blue') + f' - {display_boss(enemy)}')

    click.echo(click.style(f'BOARD:', fg='blue'))
    click.echo(show_board(state['board']))

    click.echo(click.style(f'YOU:', fg='blue') + f' - {display_hero(hero)}\n')
    click.echo(click.style(f'YOUR VALUE: ', fg='blue') + f'{state["hero"]["value"]}')