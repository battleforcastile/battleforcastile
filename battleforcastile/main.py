import os
import click

from battleforcastile.constants import DATA_FOLDER
from battleforcastile.cli.play import play
from battleforcastile.cli.cards import cards


@click.group()
def cli():
    """
    Microverse tool to:
    Check the help available for each command listed below.
    """
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


cli.add_command(play)
cli.add_command(cards)
