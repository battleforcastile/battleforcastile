class EnemyPlayerConcededException(Exception):
    pass


class EnemyPlayerHasWonException(Exception):
    pass


class HeroPlayerHasWonException(Exception):
    pass


class MatchTimeoutException(Exception):
    pass


class MatchNotFoundException(Exception):
    pass


class MatchCouldNotBeStartedException(Exception):
    pass


class MatchCouldNotBeCreatedException(Exception):
    pass


class TurnCouldNotBeSentException(Exception):
    pass