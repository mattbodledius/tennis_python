from src.game import Game


def test_game():
    game = Game('Joe', 'Jimmy')
    assert str(game) == '0-0'

    result = game.point_scored('Joe')
    assert result is None
    assert str(game) == '1-0'

    game.point_scored('Jimmy')
    assert result is None
    assert str(game) == '1-1'
