import time

import click

from battleforcastile.utils.create_match import create_match
from battleforcastile.utils.search_match import search_match


def find_or_create_match(username: str, hero: dict):
    match = None

    click.echo('Looking for another player...')
    while True:
        r = search_match(username, hero)
        if r.status_code == 200:
            match = r.json()
            click.echo('Ready to start!')
            break
        else:
            r = create_match(username, hero)
            if r.status_code == 201:
                time.sleep(5)
            else:
                click.echo('An error occurred. Please try again later.')
                break
    return match
