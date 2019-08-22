# Units
unit_card_value_2 = {
    "meta": {
        "name": "Ancient Tree",
        "type": "unit",
        "class": "creatures"
    },
    "stats": {
        "original_value": 2,
        "current_value": 2,
        "cost": 3
    },
    "skills": []
}

unit_card_value_3 = {
    "meta": {
        "name": "Monster Rat",
        "type": "unit",
        "class": "creatures"
    },
    "stats": {
        "original_value": 3,
        "current_value": 3,
        "cost": 3
    },
    "skills": []
}

# Spells
spell_card_value_minus_2_enemy_all = {
    "meta": {
        "name": "Paralyzing Poison",
        "type": "spell",
        "class": "creatures",
        "description": "Give -2 to all enemy cards on the board"
    },
    "stats": {
        "original_value": -2,
        "current_value": -2,
        "cost": 4
    },
    "selectors":  {
        "board_side": 0,
        "target": "all"
    }
}

spell_card_value_plus_2_hero_highest = {
    "meta": {
        "name": "Potion of Growth",
        "type": "spell",
        "class": "creatures",
        "description": "Give +2 to the highest value card on your side of the board"
    },
    "stats": {
        "original_value": 2,
        "current_value": 2,
        "cost": 6
    },
    "selectors":  {
        "board_side": 1,
        "target": "highest"
    }
}

spell_card_value_minus_2_enemy_highest = {
    "meta": {
        "name": "Potion of Growth",
        "type": "spell",
        "class": "creatures",
        "description": "Give -2 to the highest value card on the enemy side of the board"
    },
    "stats": {
        "original_value": -2,
        "current_value": -2,
        "cost": 6
    },
    "selectors":  {
        "board_side": 0,
        "target": "highest"
    }
}


spell_card_value_minus_2_enemy_lowest= {
    "meta": {
        "name": "Potion of Death",
        "type": "spell",
        "class": "creatures",
        "description": "Give -2 to the lowest value card on the enemy of the board"
    },
    "stats": {
        "original_value": -2,
        "current_value": -2,
        "cost": 6
    },
    "selectors":  {
        "board_side": 0,
        "target": "lowest"
    }
}