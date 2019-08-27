import json
import os

from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL
from battleforcastile.utils.delete_account import delete_account

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@patch('battleforcastile.utils.delete_account.requests.delete')
def test_if_delete_account_works_as_it_should_with_token(mocked_delete):
    mocked_delete.return_value.status_code = 200

    token = 'test'

    response = delete_account(token)

    assert response.status_code == 200
    mocked_delete.assert_called_with(
        f'{BATTLEFORCASTILE_BACKEND_URL}/account/delete/',
        data=json.dumps({
            'token': token
        }))
