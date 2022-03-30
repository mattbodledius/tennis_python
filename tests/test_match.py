

from src.match import Match


def test_match():
    new_set = Match('Joe', 'Jimmy')
    assert new_set.score() == '0-0, 0-0'

    new_set.pointWonBy('Joe')
    assert new_set.score() == '0-0, 15-0'

    new_set.pointWonBy('Joe')
    new_set.pointWonBy('Joe')
    new_set.pointWonBy('Joe')
    assert new_set.score() == '1-0, 0-0'

    close_set = Match('Joe', 'Jimmy')
    close_set.pointWonBy('Joe')
    close_set.pointWonBy('Joe')
    close_set.pointWonBy('Joe')
    close_set.pointWonBy('Jimmy')
    close_set.pointWonBy('Jimmy')
    close_set.pointWonBy('Jimmy')
    close_set.pointWonBy('Joe')
    assert close_set.score() == '0-0, Advantage Player 1'

    close_set.pointWonBy('Jimmy')
    assert close_set.score() == '0-0, Deuce'

    close_set.pointWonBy('Jimmy')
    assert close_set.score() == '0-0, Advantage Player 2'
