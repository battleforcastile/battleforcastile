from typing import List


def play_instances_from_enemy(board: List[List], instances_to_invoke: List[dict]) -> List[List]:
    enemy_board_side = 0

    board[enemy_board_side] += instances_to_invoke

    return board