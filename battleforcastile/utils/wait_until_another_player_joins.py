import time

import click

from battleforcastile.exceptions import MatchNotFoundException, MatchTimeoutException
from battleforcastile.utils.get_match_by_id import get_match_by_id


def wait_until_another_player_joins(match: dict) -> dict:
    while True:
        r = get_match_by_id(match['id'])
        if r.status_code == 200:
            match = r.json()
            if match['first_user']['username'] and match['second_user']['username']:
                click.echo('Ready to start!')
                break
            elif match['timeout'] is True:
                raise MatchTimeoutException()
        else:
            # A problem occurred
            raise MatchNotFoundException(r.content)

        time.sleep(3)
    return match