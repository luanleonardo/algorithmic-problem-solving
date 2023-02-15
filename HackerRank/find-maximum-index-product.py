# https://www.hackerrank.com/challenges/find-maximum-index-product

from sys import stdin, stdout


def maximum_index_product(N, arr):
    L, R = {}, {}
    max_product = 0

    L[1], R[1] = 0, 0
    L[N], R[N] = 0, 0

    for i in range(2, N):
        j = i - 1
        while j >= 1 and arr[j] <= arr[i]:
            j = L[j]
        L[i] = j

    for i in range(N - 1, 1, -1):
        k = i + 1
        while i < k <= N and arr[k] <= arr[i]:
            k = R[k]
        R[i] = k
        max_product = max(max_product, L[i] * R[i])

    return max_product


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    arr = [float("-inf")] + list(map(int, stdin.readline().strip().split()))
    stdout.write(f"{maximum_index_product(N, arr)}\n")
