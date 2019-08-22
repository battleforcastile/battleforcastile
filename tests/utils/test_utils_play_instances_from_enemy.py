import os

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.play_instances_from_enemy import play_instances_from_enemy


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_play_instances_from_enemy_does_what_it_should():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    cards_in_hand = select_all_files(path)
    enemy_side = 0
    hero_side = 1
    board = [[], []]

    card_to_play = cards_in_hand[enemy_side]
    instances_to_invoke = [card_to_play, card_to_play, card_to_play]

    board = play_instances_from_enemy(board, instances_to_invoke)

    assert len(board[enemy_side]) == len(instances_to_invoke)
    assert len(board[hero_side]) == 0
