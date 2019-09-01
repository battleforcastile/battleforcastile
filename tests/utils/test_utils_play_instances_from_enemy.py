from battleforcastile.utils.play_instances_from_enemy import play_instances_from_enemy
from tests.fixtures import unit_card_value_1


def test_if_play_instances_from_enemy_does_what_it_should():
    enemy_side = 0
    hero_side = 1
    board = [[], []]

    card_to_play = unit_card_value_1
    instances_to_invoke = [card_to_play, card_to_play, card_to_play]

    board = play_instances_from_enemy(board, instances_to_invoke)

    assert len(board[enemy_side]) == len(instances_to_invoke)
    assert len(board[hero_side]) == 0
