import os

__VERSION__ = '0.0.2'

CARDS_FOLDER_NAME = 'cards'

DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'
DATA_FOLDER_PATH = os.path.join(os.path.expanduser('~'), '.battleforcastile')
CARDS_FOLDER_PATH = os.path.join(DATA_FOLDER_PATH, CARDS_FOLDER_NAME)

BATTLEFORCASTILE_CONFIG_FILEPATH = os.path.join(DATA_FOLDER_PATH, os.environ.get(
    'BATTLEFORCASTILE_CONFIG_FILEPATH', 'client_config'))

CARDS_CSV_FILE_NAME  = 'battleforcastile_cards.csv'

BOSSES_FOLDER_NAME = 'bosses'
HEROES_FOLDER_NAME = 'heroes'

MAX_NUM_TURNS = 20
MAX_NUM_CARDS_IN_HAND = 5
MAX_NUM_LEVELS = 3
MAX_NUM_LEVELS_E2E = 2

HERO_BOARD_SIDE = 1
ENEMY_BOARD_SIDE = 0

BATTLEFORCASTILE_BACKEND_URL = os.getenv('BATTLEFORCASTILE_BACKEND_URL', 'https://game.battleforcastile.com/api/v1')
