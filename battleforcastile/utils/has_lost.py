def has_lost(first_character_value: int, second_character_value: int,
             num_cards_in_hand_hero: int = None, num_cards_in_hand_enemy: int = None, wins_tie: bool = False) -> bool:

    if num_cards_in_hand_hero + num_cards_in_hand_enemy == 0:
        if first_character_value < second_character_value:
            return True
        elif first_character_value == second_character_value and wins_tie is not True:
            return True

    return False