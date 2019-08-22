from click.testing import CliRunner

from battleforcastile.main import play, cards


class UtilsTest:
    runner = CliRunner()

    # Play
    @classmethod
    def play_story(cls, test_user_input=False):
        args = ['story']

        if test_user_input:
            args.append('--test-user-input')
            args.append(0)

        return cls.runner.invoke(play, args)

    # Cards
    @classmethod
    def cards_core_set(cls):
        args = ['core-set']

        return cls.runner.invoke(cards, args)