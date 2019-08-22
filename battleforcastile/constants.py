import os

__VERSION__ = '0.0.1'


DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'
DATA_FOLDER = '{}/.battleforcastile'.format(os.path.expanduser('~'))

BOSSES_FOLDER_NAME = 'bosses'
HEROES_FOLDER_NAME = 'heroes'

CARDS_FOLDER_NAME = 'cards'
CORE_SET_FOLDER_NAME = 'core_set'


MAX_NUM_TURNS = 20
MAX_NUM_CARDS_IN_HAND = 5
MAX_NUM_LEVELS = 3

HERO_BOARD_SIDE = 1
ENEMY_BOARD_SIDE = 0

BATTLEFORCASTILE_BRAIN_URL = os.getenv('BATTLEFORCASTILE_BRAIN_URL', 'http://127.0.0.1:5000/api/v1')