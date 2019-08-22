from battleforcastile.utils.select_all_files import select_all_files


def select_random_boss_by_level(path: str, level: int = 1) -> dict:
    selected_boss = None
    bosses = select_all_files(path)

    for boss in bosses:
        boss_level = boss['stats']['level']
        if boss_level == level:
            selected_boss = boss

    return selected_boss
