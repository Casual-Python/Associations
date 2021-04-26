import pytest
from associations.game import Game


@pytest.mark.parametrize("data_file", ["associations/data/words_list_eng_v1.txt"])
def test_size(data_file):
    my_game = Game(data_file=data_file)
    assert my_game.field_size == 25
