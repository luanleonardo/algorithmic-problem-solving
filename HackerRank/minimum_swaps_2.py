# https://www.hackerrank.com/challenges/minimum-swaps-2/

import itertools
from heapq import heappop, heappush
from sys import stdin, stdout

counter = itertools.count()


def minimumSwaps(arr, n):

    h = []
    outdated = {}
    for i, v in enumerate(arr):
        heappush(h, (v, -next(counter), i))
        outdated[v] = False

    total = 0
    for i in range(n - 1):
        while True:
            min_value, _, min_index = heappop(h)
            if not outdated[min_value]:
                outdated[min_value] = True
                break
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            heappush(h, (arr[min_index], -next(counter), min_index))
            total += 1
    return total


if __name__ == "__main__":

    n = int(stdin.readline().strip())

    arr = list(map(int, stdin.readline().strip().split(" ")))

    res = minimumSwaps(arr, n)

    stdout.write(f"{res}\n")
