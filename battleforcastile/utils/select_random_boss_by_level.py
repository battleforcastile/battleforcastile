import os

from battleforcastile.utils.select_all_files import select_all_files

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def select_random_boss_by_level(path: str, level: int = 1, e2e_mode: bool = False) -> dict:
    selected_boss = None

    if e2e_mode:
        return select_all_files(f'{CURRENT_PATH}/../../tests/e2e/bosses')[level - 1]
    else:
        bosses = select_all_files(path)

    for boss in bosses:
        boss_level = boss['stats']['level']
        if boss_level == level:
            selected_boss = boss

    return selected_boss
