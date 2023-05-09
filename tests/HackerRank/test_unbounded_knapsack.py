import pytest

from HackerRank.unbounded_knapsack import unbounded_knapsack


@pytest.mark.parametrize(
    "items,capacity,expected", [([1, 6, 9], 12, 12), ([3, 4, 4, 4, 8], 9, 9)]
)
def test_unbounded_knapsack_algo(items, capacity, expected):
    """test unbounded knapsack implementation"""
    assert expected == unbounded_knapsack(items=items, capacity=capacity)
