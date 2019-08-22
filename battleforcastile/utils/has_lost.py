from typing import List


def has_lost(first_character_value: int, second_character_value: int,
             cards_in_hand: List = None, wins_tie: bool = False) -> bool:
    cards_in_hand = cards_in_hand or []
    if len(cards_in_hand) == 0:
        if first_character_value < second_character_value:
            return True
        elif first_character_value == second_character_value and wins_tie is not True:
            return True

    return False