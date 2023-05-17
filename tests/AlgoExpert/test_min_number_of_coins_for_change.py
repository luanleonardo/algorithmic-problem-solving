import pytest

from AlgoExpert.min_number_of_coins_for_change import minNumberOfCoinsForChange


@pytest.mark.parametrize(
    "n,denoms,expected", [(7, [1, 5, 10], 3), (7, [2, 4], -1)]
)
def test_min_coins(n, denoms, expected):
    assert minNumberOfCoinsForChange(n=n, denoms=denoms) == expected
