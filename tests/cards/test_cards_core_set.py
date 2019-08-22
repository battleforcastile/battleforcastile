from tests.utils_test import UtilsTest


# Workflow
def test_user_can_see_cards_from_the_core_set():
    r = UtilsTest.cards_core_set()
    assert r.exit_code == 0
    assert 'These are the cards available on the Core Set:' in r.output

