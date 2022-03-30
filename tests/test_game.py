from src.game import Game


def test_game():
    game = Game('Joe', 'Jimmy')
    assert str(game) == '0-0'

    result = game.pointWonBy('Joe')
    assert result is None
    assert str(game) == '15-0'

    game.pointWonBy('Jimmy')
    game.pointWonBy('Jimmy')
    assert result is None
    assert str(game) == '15-30'
