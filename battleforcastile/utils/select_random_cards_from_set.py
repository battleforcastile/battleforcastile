import os
import random
from typing import List

from battleforcastile.utils.select_all_files import select_all_files

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def select_random_cards_from_set(path: str, max_num_cards: int, e2e_mode: bool = False) -> List:
    selected_cards = []

    if e2e_mode:
        return select_all_files(f'{CURRENT_PATH}/../../tests/e2e/cards')
    else:
        cards = select_all_files(path)

    # If the set has fewer cards than the required
    if len(cards) < max_num_cards:
        raise Exception('Card Set doesnt contain enough cards')

    while len(selected_cards) < max_num_cards:
        index = random.randrange(0, len(cards))
        card = cards[index]
        if card not in selected_cards:
            selected_cards.append(card)

    return selected_cards