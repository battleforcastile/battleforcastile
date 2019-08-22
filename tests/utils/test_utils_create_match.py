import json
import os

from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_BRAIN_URL
from battleforcastile.utils.create_match import create_match

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@patch('battleforcastile.utils.create_match.requests.post')
def test_if_create_match_works_as_it_should(mocked_post):
    mocked_post.return_value.status_code = 200

    username = 'test'
    character = {}
    response = create_match(username, character)

    assert response.status_code == 200
    mocked_post.assert_called_with(
        f'{BATTLEFORCASTILE_BRAIN_URL}/matches/',
        data=json.dumps({
            'first_user': {
                'username': username,
                'character': character
            }
        }))
