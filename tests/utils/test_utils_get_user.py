import json
import os

from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_AUTH_URL
from battleforcastile.utils.get_user import get_user

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@patch('battleforcastile.utils.get_user.requests.post')
def test_if_get_user_works_as_it_should(mocked_post):
    mocked_post.return_value.status_code = 200

    token = '11111'
    response = get_user(token)

    assert response.status_code == 200
    mocked_post.assert_called_with(
        f'{BATTLEFORCASTILE_AUTH_URL}/get_user/',
        data=json.dumps({
            'token': token
        }))
