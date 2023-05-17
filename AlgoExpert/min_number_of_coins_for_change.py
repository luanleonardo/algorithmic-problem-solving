def min_coin_change(x, capacity):
    num_items = len(x)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]
    for c in range(1, capacity + 1):
        for i in range(1, num_items + 1):
            if x[i - 1] <= c:
                dp[i][c] = max(
                    dp[i][c], dp[i][c - x[i - 1]] + x[i - 1]
                )
    import pdb; pdb.set_trace()
    return dp[num_items][capacity]


def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    return min_coin_change(x=denoms, capacity=n)
