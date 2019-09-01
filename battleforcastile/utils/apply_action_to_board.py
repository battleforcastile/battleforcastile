import copy


def apply_action_to_board(state: dict, card_to_play: dict, board_side: int) -> dict:
    """
    Board_side: 0 (Enemy side), 1 (Our side), [0, 1] (All)
    """
    # TODO: Implement when the spell affects the whole board
    # TODO: Implement when a unit does something after being played
    new_board = copy.deepcopy(state['board'])
    card_type = card_to_play['meta']['type']

    if card_type == 'unit':
        new_board[board_side].append(card_to_play)

    elif card_type == 'spell':
        board_side_target = card_to_play['selectors']['board_side']
        selection = card_to_play['selectors']['target']

        if selection == 'all':
            for idx, _ in enumerate(state['board'][board_side_target]):
                card_from_board = new_board[board_side_target][idx]
                card_from_board['stats']['current_value'] += card_to_play['stats']['current_value']

            new_board[board_side_target][:] = [
                card for card in new_board[board_side_target] if card['stats']['current_value'] > 0]

        elif selection == 'highest':
            highest_value = 0

            # Get highest value
            for idx, _ in enumerate(state['board'][board_side_target]):
                card_from_board = new_board[board_side_target][idx]
                if card_from_board['stats']['current_value'] > highest_value:
                    highest_value = card_from_board['stats']['current_value']

            highest_value_cards = []
            # Get cards with the highest value
            for idx, _ in enumerate(state['board'][board_side_target]):
                card_from_board = new_board[board_side_target][idx]
                if card_from_board['stats']['current_value'] == highest_value:
                    highest_value_cards.append(card_from_board)

            # Apply change to the selected cards
            for card in highest_value_cards:
                card['stats']['current_value'] += card_to_play['stats']['current_value']

            # Delete board if necessary
            new_board[board_side_target][:] = [
                card for card in new_board[board_side_target] if card['stats']['current_value'] > 0]


        elif selection == 'lowest':
            lowest_value = 999

            # Get lowest value
            for idx, _ in enumerate(state['board'][board_side_target]):
                card_from_board = new_board[board_side_target][idx]
                if card_from_board['stats']['current_value'] < lowest_value:
                    lowest_value = card_from_board['stats']['current_value']

            lowest_value_cards = []
            # Get cards with the lowest value
            for idx, _ in enumerate(state['board'][board_side_target]):
                card_from_board = new_board[board_side_target][idx]
                if card_from_board['stats']['current_value'] == lowest_value:
                    lowest_value_cards.append(card_from_board)

            # Apply change to the selected cards
            for card in lowest_value_cards:
                card['stats']['current_value'] += card_to_play['stats']['current_value']

            # Delete board if necessary
            new_board[board_side_target][:] = [
                card for card in new_board[board_side_target] if card['stats']['current_value'] > 0]

    state['board'] = new_board
    return state
