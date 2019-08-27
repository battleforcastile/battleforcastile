import click
from click import pass_obj

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

    create_account(email, username, password)

    click.echo('Account Created')


@account.command(help='Delete a account in Battle for Castile')
@pass_obj
def delete(config):
    if not config.token:
        click.echo('You seem to be logged out. Please log in first')
        exit(1)

    delete_account(config.token)

    click.echo('Account Deleted')