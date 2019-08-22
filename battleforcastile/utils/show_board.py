from typing import List

import click

from battleforcastile.utils.show_cards import show_cards


def show_board(board: List[List]) -> str:
    enemy_side = 0
    hero_side = 1
    output = ''

    if not board or len(board) < 2:
        raise Exception('Board has an invalid format')

    if not board[enemy_side]:
        output += '\t (empty)\n'
    else:
        output += click.style(show_cards(board[enemy_side]), fg='blue')

    output += '\t -----------------------------------------------------\n'

    if not board[hero_side]:
        output += '\t (empty)\n'
    else:
        output += click.style(show_cards(board[hero_side]), fg='blue')

    return output