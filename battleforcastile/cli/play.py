import json
import os

import click
from click import pass_obj

from battleforcastile.constants import HEROES_FOLDER_NAME, MAX_NUM_LEVELS, BOSSES_FOLDER_NAME
from battleforcastile.utils.get_user import get_user
from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.play_game import play_game
from battleforcastile.utils.select_random_boss_by_level import select_random_boss_by_level
from battleforcastile.utils.find_or_create_match import find_or_create_match
from battleforcastile.utils.play_multiplayer_game import play_multiplayer_game
from battleforcastile.utils.finish_match import finish_match

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@click.group(help='Play on single-player or multi-player mode')
@pass_obj
def play(config):
    """Play single-player or multi-player"""
    pass


@play.command(help='Play on single-player mode')
def story():
    # Set paths
    heroes_path = os.path.join(CURRENT_PATH, '..', HEROES_FOLDER_NAME)

    # Set vars
    current_level = 1
    has_finish_story_mode = False

    heroes = select_all_files(heroes_path)
    hero = heroes[0]

    click.echo('Welcome to "Battle for Castile" story mode!')

    while current_level <= MAX_NUM_LEVELS and not has_finish_story_mode:
        bosses_path = os.path.join(CURRENT_PATH, '..', BOSSES_FOLDER_NAME)
        enemy = select_random_boss_by_level(bosses_path, level=current_level)

        click.echo(click.style('============================================================', fg='cyan', bold=True))
        click.echo(click.style(f'Level {current_level}: {enemy["meta"]["name"]}', fg='cyan', bold=True))
        click.echo(click.style('============================================================', fg='cyan', bold=True))

        did_hero_win = play_game(hero, enemy)

        if did_hero_win:
            click.echo('Congrats! You won this level! :)')
            if current_level == MAX_NUM_LEVELS:
                click.echo('You finished the story mode!')
                has_finish_story_mode = True
        else:
            click.echo('You lost... Please try again!')
            break

        current_level += 1



@play.command(help='Challenge another player!')
@pass_obj
def match(config):
    if not config.token:
        click.echo('You seem to be logged out. Please log in first')
        exit(1)

    # Set paths
    heroes_path = os.path.join(CURRENT_PATH, '..', HEROES_FOLDER_NAME)
    # Set vars
    did_hero_win = False

    r = get_user(config.token)
    if r.status_code != 200:
        click.echo('A problem has occurred. Please try again later.')
        exit(1)

    username = r.json()['username']
    click.echo(f'Hello {username}!')

    # Set random hero for now (This should change later on)
    heroes = select_all_files(heroes_path)
    hero = heroes[0]

    # TODO: Create unittest
    match = find_or_create_match(username, hero)

    if not match:
        click.echo('A problem has occurred. Please try again later.')
        exit(1)

    enemy_info, should_start = (match['first_user'], True) if \
                                match['first_user']['username'] != username else (
                                match['second_user'], False)
    try:
        did_hero_win = play_multiplayer_game(
            hero=hero,
            enemy=json.loads(enemy_info['character']),
            should_start=should_start,
            match_id=match['id'],
            hero_username=username,
            enemy_username=enemy_info['username']
        )
    except:
        click.echo('A problem has occurred. Please try again later.')
        finish_match(match['id'])

    if did_hero_win:
        finish_match(match['id'], username)
        click.echo('Congrats! You won! :)')
    else:
        click.echo('You lost... Let\'s try again!')

