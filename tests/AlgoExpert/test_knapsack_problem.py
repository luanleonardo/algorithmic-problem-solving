from AlgoExpert.knapsack_problem import knapsackProblem


def test_knapsack_solver():
    items, capacity = [[3, 4], [2, 3], [4, 2]], 5
    expected_result = [6, [2, 1]]

    assert expected_result == knapsackProblem(items, capacity)
