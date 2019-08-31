from typing import List

import click

from battleforcastile.constants import HERO_BOARD_SIDE
from battleforcastile.utils.apply_action_to_board import apply_action_to_board
from battleforcastile.utils.display_match_state import display_match_state
from battleforcastile.utils.show_cards import show_cards
from battleforcastile.utils.display_card import display_card
from battleforcastile.utils.show_options import show_options


def play_hero_turn(turn_number: int, state: dict, cards_in_hand: List) -> (dict, List):
    click.echo(click.style(f'CARDS IN HAND:', fg='blue'))
    click.echo(show_cards(cards_in_hand, with_indices=True, with_cost=True))

    card_to_play = show_options(cards_in_hand, turn_number)

    if card_to_play:
        cards_in_hand.remove(card_to_play)
        state = apply_action_to_board(state, card_to_play, HERO_BOARD_SIDE)

        click.echo(click.style(f'ACTION THIS TURN: ', fg='blue') + f'{display_card(card_to_play)}')
    else:
        click.echo(click.style(f'ACTION THIS TURN: ', fg='blue') + f'-')

    return state, cards_in_hand
