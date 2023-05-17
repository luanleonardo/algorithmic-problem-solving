# https://www.algoexpert.io/questions/min-number-of-coins-for-change


def min_coin_change(x, R):
    n = len(x)
    dp = [[float("inf") for _ in range(R + 1)] for _ in range(n)]

    for m in range(R + 1):
        if m % x[0] == 0:
            dp[0][m] = m // x[0]

    for i in range(1, n):
        for m in range(R + 1):
            if x[i] <= m and dp[i][m - x[i]] + 1 < dp[i - 1][m]:
                dp[i][m] = dp[i][m - x[i]] + 1
            else:
                dp[i][m] = dp[i - 1][m]

    return dp[n - 1][R]


def minNumberOfCoinsForChange(n, denoms):
    result = min_coin_change(x=denoms, R=n)
    return result if result != float("inf") else -1
