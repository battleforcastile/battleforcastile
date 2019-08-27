import json

import requests

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL

def delete_account(token: str):
    url = f'{BATTLEFORCASTILE_BACKEND_URL}/account/delete/'
    return requests.delete(url, data=json.dumps({
        'token': token,
    }))