import json
import os

from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL
from battleforcastile.utils.join_match import join_match

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@patch('battleforcastile.utils.join_match.requests.post')
def test_if_join_match_works_as_it_should(mocked_post):
    mocked_post.return_value.status_code = 200

    username = 'test'
    character = {}

    response = join_match(username, character)

    assert response.status_code == 200
    mocked_post.assert_called_with(
        f'{BATTLEFORCASTILE_BACKEND_URL}/matches/join/',
        data=json.dumps({
            'user': {
                'username': username,
                'character': character
            }
        }))
