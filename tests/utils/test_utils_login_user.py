import json

from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL
from battleforcastile.utils.login_user import login_user


@patch('battleforcastile.utils.login_user.requests.post')
def test_if_login_works_as_it_should(mocked_post):
    mocked_post.return_value.status_code = 200

    username = 'test'
    password = 'test'

    response = login_user(username, password)

    assert response.status_code == 200
    mocked_post.assert_called_with(
        f'{BATTLEFORCASTILE_BACKEND_URL}/account/login/',
        data=json.dumps({
            'username': username,
            'password': password
        }))
