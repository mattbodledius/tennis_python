

from src.match import Match


def test_match():
    new_set = Match('Joe', 'Jimmy')
    assert str(new_set) == '0-0, 0-0'

    new_set.pointBy('Joe')
    assert str(new_set) == '0-0, 1-0'

    new_set.pointBy('Joe')
    new_set.pointBy('Joe')
    new_set.pointBy('Joe')
    new_set.pointBy('Joe')
    new_set.pointBy('Joe')
    assert str(new_set) == '1-0, 0-0'
