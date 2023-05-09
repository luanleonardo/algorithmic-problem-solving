# https://www.hackerrank.com/challenges/unbounded-knapsack/problem?isFullScreen=false

# from sys import stdin, stdout


def unbounded_knapsack(items, capacity):
    optimal_value = [0] * (capacity + 1)
    for c in range(1, capacity + 1):
        for w in items:
            if w <= c:
                optimal_value[c] = max(
                    optimal_value[c], optimal_value[c - w] + w
                )
    return optimal_value[capacity]


# if __name__ == "__main__":
#     t = int(stdin.readline().strip())
#     for _ in range(t):
#         n, k = map(int, stdin.readline().strip().split())
#         arr = list(map(int, stdin.readline().strip().split()))
#         stdout.write(f"{unbounded_knapsack(items=arr, capacity=k)}\n")
