from battleforcastile.utils.has_lost import has_lost


def test_if_has_lost_is_true_when_character_has_lower_value_and_an_empty_hand():
    state = {
        'hero': {
            'value': 10
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    num_cards_in_hand_hero = 0
    num_cards_in_hand_enemy = 0

    assert has_lost(state['hero']['value'], state['enemy']['value'],
                    num_cards_in_hand_hero, num_cards_in_hand_enemy) is True


def test_if_has_lost_is_false_when_character_has_lower_value_but_not_an_empty_hand():
    state = {
        'hero': {
            'value': 10
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    num_cards_in_hand_hero = 1
    num_cards_in_hand_enemy = 0
    assert has_lost(state['hero']['value'], state['enemy']['value'],
                    num_cards_in_hand_hero, num_cards_in_hand_enemy) is False


def test_if_has_lost_is_false_when_character_has_bigger_value_and_an_empty_hand():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 10
        }
    }
    num_cards_in_hand_hero = 0
    num_cards_in_hand_enemy = 0
    assert has_lost(state['hero']['value'], state['enemy']['value'],
                    num_cards_in_hand_hero, num_cards_in_hand_enemy) is False


def test_if_has_lost_is_false_when_character_has_bigger_value_and_not_an_empty_hand():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 10
        }
    }
    num_cards_in_hand_hero = 1
    num_cards_in_hand_enemy = 0
    assert has_lost(state['hero']['value'], state['enemy']['value'],
                    num_cards_in_hand_hero, num_cards_in_hand_enemy) is False


def test_if_has_lost_is_true_when_character_has_equal_value_an_empty_hand_and_wins_tie_false():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    num_cards_in_hand_hero = 0
    num_cards_in_hand_enemy = 0
    assert has_lost(state['hero']['value'], state['enemy']['value'],
                    num_cards_in_hand_hero, num_cards_in_hand_enemy, wins_tie=False) is True


def test_if_has_lost_is_false_when_character_has_equal_value_an_empty_hand_and_wins_tie_true():
    state = {
        'hero': {
            'value': 20
        },
        'board': [[], []],
        'enemy': {
            'value': 20
        }
    }
    num_cards_in_hand_hero = 0
    num_cards_in_hand_enemy = 0
    assert has_lost(state['hero']['value'], state['enemy']['value'],
                    num_cards_in_hand_hero, num_cards_in_hand_enemy, wins_tie=True) is False
