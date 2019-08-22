from typing import List


def calculate_current_value(cards: List[dict]) -> (int):
    total_value = 0

    for card in cards:
        value = card['stats']['current_value']
        total_value += value

    return total_value