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
                if card_from_board['stats']['current_value'] <= 0:
                    del new_board[board_side_target][idx]
        elif selection == 'highest':
            highest_value = 0
            highest_value_card_idx = None
            for idx, _ in enumerate(state['board'][board_side_target]):
                card_from_board = new_board[board_side_target][idx]
                if card_from_board['stats']['current_value'] > highest_value:
                    highest_value = card_from_board['stats']['current_value']
                    highest_value_card_idx = idx

            if highest_value_card_idx is not None:
                new_board[board_side_target][highest_value_card_idx]['stats']['current_value'] += (
                    card_to_play['stats']['current_value'])
                if new_board[board_side_target][highest_value_card_idx]['stats']['current_value'] <= 0:
                    del new_board[board_side_target][highest_value_card_idx]

        elif selection == 'lowest':
            lowest_value = 999
            lowest_value_card_idx = None
            for idx, _ in enumerate(state['board'][board_side_target]):
                card_from_board = new_board[board_side_target][idx]
                if card_from_board['stats']['current_value'] < lowest_value:
                    lowest_value = card_from_board['stats']['current_value']
                    lowest_value_card_idx = idx

            if lowest_value_card_idx is not None:
                new_board[board_side_target][lowest_value_card_idx]['stats']['current_value'] += (
                    card_to_play['stats']['current_value'])
                if new_board[board_side_target][lowest_value_card_idx]['stats']['current_value'] <= 0:
                    del new_board[board_side_target][lowest_value_card_idx]

    state['board'] = new_board
    return state
