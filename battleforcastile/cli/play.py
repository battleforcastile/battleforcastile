import json
import os

import click
from click import pass_obj

from battleforcastile.constants import HEROES_FOLDER_NAME, MAX_NUM_LEVELS, BOSSES_FOLDER_NAME, MAX_NUM_LEVELS_E2E, \
    CARDS_FOLDER_PATH, CARDS_CSV_FILE_NAME
from battleforcastile.exceptions import EnemyPlayerConcededException, EnemyPlayerHasWonException, \
    HeroPlayerHasWonException, MatchTimeoutException, MatchNotFoundException, MatchCouldNotBeCreatedException, \
    TurnCouldNotBeSentException, MatchCouldNotBeStartedException
from battleforcastile.scripts.generate_cards_from_csv import read_csv, create_file_structure
from battleforcastile.utils.wait_until_another_player_joins import wait_until_another_player_joins
from battleforcastile.utils.get_user import get_user
from battleforcastile.utils.select_all_files import select_all_files
from battleforcastile.utils.play_game import play_game
from battleforcastile.utils.select_random_boss_by_level import select_random_boss_by_level
from battleforcastile.utils.find_or_create_match import find_or_create_match
from battleforcastile.utils.play_multiplayer_game import play_multiplayer_game
from battleforcastile.utils.finish_match import finish_match
from battleforcastile.utils.start_match import start_match

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@click.group(help='Play on single-player or multi-player mode')
@pass_obj
def play(config):
    """Play single-player or multi-player"""
    pass


@play.command(help='Play on single-player mode')
@click.option('--e2e-mode', type=click.BOOL, required=False)
@pass_obj
def story(config, e2e_mode):
    # Set paths
    heroes_path = os.path.join(CURRENT_PATH, '..', HEROES_FOLDER_NAME)

    # Generate cards
    cards = read_csv(os.path.join(CURRENT_PATH, '..', CARDS_CSV_FILE_NAME))
    create_file_structure(path=CARDS_FOLDER_PATH, cards=cards)

    # Set vars
    current_level = 1
    has_finish_story_mode = False

    if e2e_mode:
        hero = select_all_files(f'{CURRENT_PATH}/../../tests/e2e/heroes')[0]
    else:
        heroes = select_all_files(heroes_path)
        hero = heroes[0]

    click.echo('Welcome to "Battle for Castile" story mode!')

    while current_level <= MAX_NUM_LEVELS and not has_finish_story_mode:
        bosses_path = os.path.join(CURRENT_PATH, '..', BOSSES_FOLDER_NAME)
        enemy = select_random_boss_by_level(bosses_path, level=current_level, e2e_mode=e2e_mode)

        click.echo(click.style('============================================================', fg='cyan', bold=True))
        click.echo(click.style(f'Level {current_level}: {enemy["meta"]["name"]}', fg='cyan', bold=True))
        click.echo(click.style('============================================================', fg='cyan', bold=True))

        did_hero_win = play_game(hero, enemy, e2e_mode)

        if did_hero_win:
            click.echo('Congrats! You won this level! :)')
            if current_level == MAX_NUM_LEVELS or (current_level == MAX_NUM_LEVELS_E2E and e2e_mode is True):
                click.echo('You finished the story mode!')
                has_finish_story_mode = True
        else:
            click.echo('You lost... Please try again!')
            break

        current_level += 1



@play.command(help='Challenge another player!')
@click.option('--e2e-mode', type=click.BOOL, required=False)
@pass_obj
def match(config, e2e_mode):
    if not config.token:
        click.echo('You seem to be logged out. Please log in first')
        exit(1)

    # Set paths
    heroes_path = os.path.join(CURRENT_PATH, '..', HEROES_FOLDER_NAME)

    # Generate cards
    cards = read_csv(os.path.join(CURRENT_PATH, '..', CARDS_CSV_FILE_NAME))
    create_file_structure(path=CARDS_FOLDER_PATH, cards=cards)

    # Set vars
    match = None

    r = get_user(config.token)
    if r.status_code != 200:
        click.echo('A problem has occurred. Please try again later.')
        exit(1)

    username = r.json()['username']
    click.echo(f'Hello {username}!')

    # Set random hero for now (This should change later on)
    if e2e_mode:
        hero = select_all_files(f'{CURRENT_PATH}/../../tests/e2e/heroes')[0]
    else:
        heroes = select_all_files(heroes_path)
        hero = heroes[0]

    # TODO: Create unittest
    try:
        match = find_or_create_match(username, hero)

    except MatchCouldNotBeCreatedException:
        click.echo('The Match could not be created. Please try again later.')
        exit(1)

    except MatchNotFoundException:
        click.echo('[IMPORTANT] There was a problem while fetching the Match. Please try again later.')
        exit(1)

    try:
        # TODO: Create unittest
        match = wait_until_another_player_joins(match)

    except MatchNotFoundException:
        click.echo('[IMPORTANT] There was a problem while fetching the Match. Please try again later.')
        finish_match(match['id'])
        exit(1)

    except MatchTimeoutException:
        click.echo('[IMPORTANT] We couldn\'t find a player. Please try again later.')
        finish_match(match['id'])
        exit(1)

    try:
        # TODO: Create unittest
        start_match(match['id'])
    except MatchCouldNotBeStartedException:
        click.echo('[IMPORTANT] The Match could not be started. Please try again later.')
        finish_match(match['id'])
        exit(1)

    enemy_info, should_start = (match['first_user'], True) if \
                                match['first_user']['username'] != username else (
                                match['second_user'], False)
    try:
        play_multiplayer_game(
            hero=hero,
            enemy=json.loads(enemy_info['character']),
            should_start=should_start,
            match_id=match['id'],
            hero_username=username,
            enemy_username=enemy_info['username'],
            e2e_mode=e2e_mode
        )

    except MatchNotFoundException:
        click.echo('\n[IMPORTANT] A technical issue has occurred while fetching the Match. Unfortunately, you lost the game.')
        finish_match(match['id'])
        exit(0)

    except TurnCouldNotBeSentException:
        click.echo('\n[IMPORTANT] A technical issue has occurred while sending your Turn. Unfortunately, you lost the game.')
        finish_match(match['id'])
        exit(0)

    except EnemyPlayerHasWonException:
        click.echo('\n[IMPORTANT] The enemy has won. Better luck next time!')
        click.echo('\n[NOTICE] When the total value is the same for both players, the player who started the match wins')
        exit(0)

    except EnemyPlayerConcededException:
        click.echo('\n[IMPORTANT] The enemy has conceded. You win!')
        finish_match(match['id'], username)
        exit(0)

    except HeroPlayerHasWonException:
        click.echo('\n[IMPORTANT] You win this game. Congrats! :)')
        finish_match(match['id'], username)
        exit(0)

    except KeyboardInterrupt:
        click.echo('\n[IMPORTANT] It looks like you have conceded by pressing Control + C. Best luck next time!')
        finish_match(match['id'])
        exit(0)
