import time

import click

from battleforcastile.exceptions import MatchCouldNotBeCreatedException, MatchNotFoundException
from battleforcastile.utils.create_match import create_match
from battleforcastile.utils.get_latest_non_started_match_created_by_username import get_latest_non_started_match_created_by_username
from battleforcastile.utils.join_match import join_match


def find_or_create_match(username: str, hero: dict) -> dict:
    # 1) We try to join an existing match create by another user
    r = join_match(username, hero)
    if r.status_code == 200:
        match = r.json()
        return match

    # 2) If it's not possible, we create a new match
    r = create_match(username, hero)
    if r.status_code == 201:
        time.sleep(2)
    else:
        raise MatchCouldNotBeCreatedException()

    # 3) Get match created just above
    r = get_latest_non_started_match_created_by_username(username)
    if r.status_code == 200:
        click.echo('Waiting for another player...')

        matches = r.json()
        if len(matches) > 0:
            return matches[0]
        else:
            raise MatchNotFoundException()

    else:
        raise MatchNotFoundException()
