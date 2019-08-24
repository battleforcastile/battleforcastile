import json
import os

from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_AUTH_URL
from battleforcastile.utils.create_account import create_account

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@patch('battleforcastile.utils.create_account.requests.post')
def test_if_create_account_works_as_it_should(mocked_post):
    mocked_post.return_value.status_code = 200

    username = 'test'
    email = 'test@example.com'
    password = 'test'

    response = create_account(email, username, password)

    assert response.status_code == 200
    mocked_post.assert_called_with(
        f'{BATTLEFORCASTILE_AUTH_URL}/users/',
        data=json.dumps({
            'email': email,
            'username': username,
            'password': password
        }))
