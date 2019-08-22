import glob
import json
import os
import random
from typing import List


def select_all_files(path: str) -> List:
    files = glob.glob(os.path.join(path, '*.json'))

    imported_files = []
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            imported_files.append(data)

    random.shuffle(imported_files)
    return imported_files
