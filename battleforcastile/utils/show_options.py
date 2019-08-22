from typing import List

import click


def show_options(cards_in_hand: List, cost_available: int, test_user_input: int = None) -> dict:
    value = None
    card_to_play_now = {}
    counter = 0

    while card_to_play_now == {} and value != '' and counter < 10:
        if test_user_input is not None:
            value = test_user_input
        else:
            value = input('What card would you like to play? (Press ENTER to PLAY NOTHING) ')
        if value == '' or value == 0:
            card_to_play_now = {}
        else:
            try:
                value = int(value)
                card_to_play_now = cards_in_hand[value - 1]
            except Exception as e:
                click.echo('Invalid option')
            else:
                if card_to_play_now['stats']['cost'] > cost_available:
                    click.echo('Cost too high')
                    card_to_play_now = {}
        counter += 1
    return card_to_play_now