def generate_turn(turn_number: int, state: dict, hero_username: str, enemy_username: str, num_cards_in_hand_left: int):
    return {
        'number': turn_number,
        'hero': hero_username,
        'enemy': enemy_username,
        'state': state,
        'num_cards_in_hand_left': num_cards_in_hand_left
    }