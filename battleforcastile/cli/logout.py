import os

import click

from battleforcastile.constants import BATTLEFORCASTILE_CONFIG_FILENAME


@click.command(help='Logout')
def logout():
    if os.path.exists(BATTLEFORCASTILE_CONFIG_FILENAME):
        click.echo('Logout Succeeded')
        os.remove(BATTLEFORCASTILE_CONFIG_FILENAME)
    else:
        click.echo('You are already logged out')
        exit(1)
