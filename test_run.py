import pytest

from run import check_possible_game_ids, check_possible_reason

def test_check_possible_game_ids():
    assert check_possible_game_ids(11)


def test_check_possible_reason():
    with pytest.raises(TypeError):
        check_possible_reason(9)