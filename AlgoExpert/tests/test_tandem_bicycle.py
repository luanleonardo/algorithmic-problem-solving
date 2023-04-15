import pytest

from AlgoExpert.solutions.tandem_bicycle import tandemBicycle


@pytest.mark.parametrize("fastest,expected", [(True, 32), (False, 25)])
def test_tandemBicycle(fastest, expected):
    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    actual = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
    assert actual == expected
