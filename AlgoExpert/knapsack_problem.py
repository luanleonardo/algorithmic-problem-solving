# https://www.algoexpert.io/questions/knapsack-problem


# O(nC) time | O(nC) space, n = number of items, C = knapsack capacity
def knapsackProblem(items, max_capacity):
    total_items = len(items)
    optimal_value = [
        [0 for _ in range(max_capacity + 1)] for _ in range(total_items + 1)
    ]
    for i in range(1, total_items + 1):
        for c in range(1, max_capacity + 1):
            if items[i - 1][1] > c:
                optimal_value[i][c] = optimal_value[i - 1][c]
            else:
                optimal_value[i][c] = max(
                    optimal_value[i - 1][c],
                    optimal_value[i - 1][c - items[i - 1][1]]
                    + items[i - 1][0],
                )
    optimal_solution_indices = []
    c = max_capacity
    for i in range(total_items, 0, -1):
        if (
            items[i - 1][1] <= c
            and optimal_value[i - 1][c - items[i - 1][1]] + items[i - 1][0]
            >= optimal_value[i - 1][c]
        ):
            optimal_solution_indices.append(i - 1)
            c = c - items[i - 1][1]

    return [optimal_value[total_items][max_capacity], optimal_solution_indices]
