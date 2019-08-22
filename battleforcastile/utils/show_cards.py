from battleforcastile.utils.display_card import display_card
from typing import List


def show_cards(cards: List, with_indices=False, with_cost=False) -> str:
    output = ''
    for idx, card in enumerate(cards):
        if with_indices:
            output += f'\t{idx + 1}) '
        else:
            output += '\t'
        output += f'{display_card(card, with_cost=with_cost)}\n'

    return output