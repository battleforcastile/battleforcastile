import os

import click
from click import pass_obj

from battleforcastile.constants import BATTLEFORCASTILE_CONFIG_FILENAME
from battleforcastile.utils.create_account import create_account
from battleforcastile.utils.delete_account import delete_account


@click.group(help='List and modify your account details')
@pass_obj
def account(config):
    """List and modify account details."""
    pass


@account.command(help='Create a new account in Battle for Castile')
@click.option('--email', required=True)
@click.option('--username', required=True)
@pass_obj
def create(config, email, username):
    password = click.prompt('Please enter a password', type=str)

    r = create_account(email, username, password)

    if r.status_code == 201:
        click.echo('Account Created')
    else:
        click.echo(r.content)



@account.command(help='Delete a account in Battle for Castile')
@pass_obj
def delete(config):
    if not config.token:
        click.echo('You seem to be logged out. Please log in first')
        exit(1)

    r = delete_account(config.token)

    if r.status_code == 204:
        if os.path.exists(BATTLEFORCASTILE_CONFIG_FILENAME):
            os.remove(BATTLEFORCASTILE_CONFIG_FILENAME)
        click.echo('Account Deleted')
    else:
        click.echo(r.content)
