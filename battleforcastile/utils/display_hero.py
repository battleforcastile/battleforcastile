def display_hero(boss: dict) -> str:
    name = boss['meta']['name']
    level = boss['stats']['level']

    return f'{name} (Level: {level})'