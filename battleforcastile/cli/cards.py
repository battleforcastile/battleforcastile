import click
import os

from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.display_card import display_card

from battleforcastile.constants import CARDS_FOLDER_NAME, CORE_SET_FOLDER_NAME

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@click.group(help='List of cards in the game')
def cards():
    """List of cards in the game"""
    pass


@cards.command(help='List of cards on the Core Set collection')
def core_set():
    click.echo('These are the cards available on the Core Set:')

    creatures_core_set_path = os.path.join(CURRENT_PATH, '..', CARDS_FOLDER_NAME,
                                           CORE_SET_FOLDER_NAME, 'creatures')
    kingdom_core_set_path = os.path.join(CURRENT_PATH, '..', CARDS_FOLDER_NAME,
                                         CORE_SET_FOLDER_NAME, 'kingdom')
    outlaws_core_set_path = os.path.join(CURRENT_PATH, '..', CARDS_FOLDER_NAME,
                                         CORE_SET_FOLDER_NAME, 'outlaws')
    click.echo('Creatures:')
    imported_cards = select_all_files(creatures_core_set_path)
    for card in imported_cards:
        click.echo(display_card(card))

    click.echo('Kingdom:')
    imported_cards = select_all_files(kingdom_core_set_path)
    for card in imported_cards:
        click.echo(display_card(card))

    click.echo('Outlaws:')
    imported_cards = select_all_files(outlaws_core_set_path)
    for card in imported_cards:
        click.echo(display_card(card))