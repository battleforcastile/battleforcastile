import os

from unittest.mock import patch

from battleforcastile.constants import BATTLEFORCASTILE_MATCH_RECORDER_URL
from battleforcastile.utils.get_match_info import get_match_info

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


@patch('battleforcastile.utils.get_match_info.requests.get')
def test_if_get_match_info_works_as_it_should(mocked_get):
    mocked_get.return_value.status_code = 200

    match_id = 1
    get_match_info(match_id)

    mocked_get.assert_called_with(
        f'{BATTLEFORCASTILE_MATCH_RECORDER_URL}/matches/{match_id}/')
