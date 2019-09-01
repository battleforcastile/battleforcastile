from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_BACKEND_URL
from battleforcastile.utils.get_match_by_id import get_match_by_id


@patch('battleforcastile.utils.get_match_by_id.requests.get')
def test_if_get_match_by_id_works_as_it_should(mocked_get):
    mocked_get.return_value.status_code = 200

    match_id = 1
    get_match_by_id(match_id)

    mocked_get.assert_called_with(
        f'{BATTLEFORCASTILE_BACKEND_URL}/matches/{match_id}/')
