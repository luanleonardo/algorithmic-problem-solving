from sys import stdin, stdout


def knapsack(num_items, items_weights, items_values, knapsack_capacity):
    optimal_value = [
        [0 for _ in range(knapsack_capacity + 1)] for _ in range(num_items + 1)
    ]
    for i in range(1, num_items + 1):
        for c in range(1, knapsack_capacity + 1):
            if items_weights[i] > c:
                optimal_value[i][c] = optimal_value[i - 1][c]
            else:
                optimal_value[i][c] = max(
                    optimal_value[i - 1][c],
                    optimal_value[i - 1][c - items_weights[i]]
                    + items_values[i],
                )
    return optimal_value[num_items][knapsack_capacity]


# if __name__ == "__main__":
#     s, n = map(int, stdin.readline().strip().split())
#     ws = [None]
#     vs = [None]
#     for _ in range(n):
#         w, v = map(int, stdin.readline().strip().split())
#         ws.append(w)
#         vs.append(v)
#     stdout.write(
#         f"{knapsack(num_items=n, items_weights=ws, items_values=vs, knapsack_capacity=s)}"
#     )
