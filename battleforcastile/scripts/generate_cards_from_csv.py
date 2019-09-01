import csv
import json
import os
import shutil
import sys
from typing import List

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

CARDS_PATH = os.path.join(CURRENT_PATH, '..', 'cards')


def convert_name(name: str = None):
    return name.lower().replace(' ', '_')

def create_unit_file(path: str = None, card: dict = None):
    if not path:
        raise Exception('Please provide a path')

    filename = convert_name(card['name'])
    filepath = os.path.join(path, card['class'], filename)
    with open(f'{filepath}.json', 'w') as file:
        body = {
            'meta': {
                'name': card['name'],
                'type': card['type'],
                'class': card['class'],
                'set_name': card['set_name']
            },
            'stats': {
                'original_value': int(card['value']),
                'current_value': int(card['value']),
                'cost': int(card['cost'])
            }
        }
        file.write(json.dumps(body))


def create_spell_file(path: str = None, card: dict = None):
    if not path:
        raise Exception('Please provide a path')

    filename = convert_name(card['name'])
    filepath = os.path.join(path, card['class'], filename)
    with open(f'{filepath}.json', 'w') as file:
        body = {
            'meta': {
                'name': card['name'],
                'type': card['type'],
                'class': card['class'],
                'description': card['description'],
                'set_name': card['set_name']
            },
            'stats': {
                'original_value': int(card['value']),
                'current_value': int(card['value']),
                'cost': int(card['cost'])
            },
            'selectors': {
                'board_side': int(card['board_side']),
                'target': card['target'],
                'num_entities': int(card['num_entities']) if card.get('num_entities') else None,
                'entity_to_invoke': card['entity_to_invoke'] if card.get('entity_to_invoke') else None
            }
        }
        file.write(json.dumps(body))


def read_csv(filename: str = None) -> List[dict]:
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        cards = [row for row in reader]
    return cards


def create_file_structure(path: str = None, cards: List[dict] = None):
    if not path:
        raise Exception('Please provide a path')

    if os.path.exists(path):
        shutil.rmtree(path)

    os.makedirs(path)
    os.makedirs(os.path.join(path, 'creatures'))
    os.makedirs(os.path.join(path, 'kingdom'))
    os.makedirs(os.path.join(path, 'outlaws'))

    for card in cards:
        if card['type'] == 'unit':
            create_unit_file(path=path, card=card)
        elif card['type'] == 'spell':
            create_spell_file(path=path, card=card)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide at least one CSV by args')
        exit(1)

    filename = sys.argv[1]

    cards = read_csv(filename)
    create_file_structure(path=CARDS_PATH, cards=cards)
    print('All cards were created!')