# Units

unit_card_value_1 = {
    "meta": {
        "name": "Minion",
        "type": "unit",
        "class": "creatures"
    },
    "stats": {
        "original_value": 1,
        "current_value": 1,
        "cost": 1
    },
    "skills": []
}

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


spell_card_value_minus_999_enemy_all= {
    "meta": {
        "name": "Sure Death",
        "type": "spell",
        "class": "creatures",
        "description": "Destroy all the enemy of the board"
    },
    "stats": {
        "original_value": -999,
        "current_value": -999,
        "cost": 8
    },
    "selectors":  {
        "board_side": 0,
        "target": "all"
    }
}


# Bosses

black_angel = {
    "meta": {
        "name": "Black Angel"
    },
    "stats": {
        "level": 1,
        "life": 20
    },
    "powers": [
        {
            "name": "Day of death",
            "invocation": {
                "card_name": "Ancient Tree",
                "num_instances": 2
            },
            "cost": 3
        },
        {
            "name": "Day of destruction",
            "invocation": {
                "card_name": "Ancient Tree",
                "num_instances": 3
            },
            "cost": 5
        },
        {
            "name": "Armageddon",
            "invocation": {
                "card_name": "Ancient Tree",
                "num_instances": 4
            },
            "cost": 8
        }
    ]
}

giant_troll = {
    "meta": {
        "name": "Giant Troll"
    },
    "stats": {
        "level": 2,
        "life": 25
    },
    "powers": [
        {
            "name": "Smash",
            "invocation": {
                "card_name": "Furious Goblin",
                "num_instances": 2
            },
            "cost": 3
        },
        {
            "name": "Double Smash",
            "invocation": {
                "card_name": "Conjuring Fairy",
                "num_instances": 4
            },
            "cost": 4
        }
    ]
}

# Heroes

black_forest_elf = {
    "meta": {
        "name": "Black Forest Elf",
        "class": "creatures"
    },
    "stats": {
        "level": 1
    },
    "powers": []
}
