import os

from battleforcastile.utils.select_card_by_name import select_card_by_name

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_if_card_can_be_selected_when_card_exists():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    name = "Ancient Tree"
    card = select_card_by_name(path, name)
    assert card == {
        "meta": {
            "name": "Ancient Tree",
            "type": "unit",
            "class": "creatures"
        },
        "stats": {
            "original_value": 3,
            "current_value": 3,
            "cost": 1
        },
        "skills": []
    }


def test_if_we_get_empty_dict_when_card_doesnt_exists():
    path = os.path.join(CURRENT_PATH, 'fixtures', 'cards')
    name = 'Random name'
    card = select_card_by_name(path, name)
    assert card == {}
