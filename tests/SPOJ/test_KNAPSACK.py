from SPOJ.KNAPSACK import knapsack


def test_knapsack():
    num_items = 5
    capacity = 4
    weights = [None, 1, 2, 3, 2, 2]
    values = [None, 8, 4, 0, 5, 3]
    expected_result = 13

    assert expected_result == knapsack(num_items, weights, values, capacity)
