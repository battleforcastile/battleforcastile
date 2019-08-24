import os
import click

from battleforcastile.config import pass_config
from battleforcastile.constants import DATA_FOLDER, BATTLEFORCASTILE_CONFIG_FILENAME, __VERSION__
from battleforcastile.cli.play import play
from battleforcastile.cli.account import account
from battleforcastile.cli.login import login
from battleforcastile.cli.logout import logout
from battleforcastile.cli.cards import cards


def _read_user_token():
    """
    Read user token from the DATA_FOLDER.
    """
    if not os.path.exists(BATTLEFORCASTILE_CONFIG_FILENAME):
        return None
    with open(BATTLEFORCASTILE_CONFIG_FILENAME, 'r') as f:
        token = f.read()
    return token


def _get_cli_version():
    """
    Returns the CLI version.
    """
    return __VERSION__


@click.group()
@pass_config
def cli(config):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    config.token = _read_user_token()
    config.version = _get_cli_version()

cli.add_command(play)
cli.add_command(cards)
cli.add_command(account)
cli.add_command(login)
cli.add_command(logout)

