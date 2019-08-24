
import click

from battleforcastile.constants import BATTLEFORCASTILE_CONFIG_FILENAME
from battleforcastile.utils.login_user import login_user


@click.command(help='Login into Battle for Castile')
@click.option('--username', required=True)
def login(username):
    password = click.prompt('Please enter your password', type=str)

    r = login_user(username, password)

    if r.status_code == 200:
        click.echo('Login Succeeded')
        result = r.json()
        with open(BATTLEFORCASTILE_CONFIG_FILENAME, 'w+') as f:
            f.write(result.get('token'))
    else:
        click.echo(r.content)
        exit(1)
