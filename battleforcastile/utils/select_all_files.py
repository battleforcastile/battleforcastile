import json
import random
from pathlib import Path
from typing import List


def select_all_files(path: str) -> List:
    imported_files = []
    for filename in Path(path).glob('**/*.json'):

        with open(str(filename)) as json_file:
            data = json.load(json_file)
            imported_files.append(data)

    random.shuffle(imported_files)
    return imported_files
