from associations.game import Game


def test_size():
    my_game = Game()
    assert my_game.field_size == 25
