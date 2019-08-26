import os

__VERSION__ = '0.0.2'


DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'
DATA_FOLDER = '{}/.battleforcastile'.format(os.path.expanduser('~'))

BATTLEFORCASTILE_CONFIG_FILENAME = '{}/{}'.format(DATA_FOLDER, os.environ.get(
    'BATTLEFORCASTILE_CONFIG_FILENAME', 'client_config'))

BOSSES_FOLDER_NAME = 'bosses'
HEROES_FOLDER_NAME = 'heroes'

CARDS_FOLDER_NAME = 'cards'
CORE_SET_FOLDER_NAME = 'core_set'


MAX_NUM_TURNS = 20
MAX_NUM_CARDS_IN_HAND = 5
MAX_NUM_LEVELS = 3

HERO_BOARD_SIDE = 1
ENEMY_BOARD_SIDE = 0

BATTLEFORCASTILE_BACKEND_URL = os.getenv('BATTLEFORCASTILE_BACKEND_URL', 'https://game.battleforcastile.com/api/v1')
