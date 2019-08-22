from battleforcastile.utils.select_all_files import select_all_files


def select_card_by_name(path: str, name: str) -> dict:
    selected_card = {}
    cards = select_all_files(path)

    for card in cards:
        if card['meta']['name'] == name:
            selected_card = card
            break
    return selected_card