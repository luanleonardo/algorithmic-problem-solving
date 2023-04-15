# https://www.hackerrank.com/challenges/x-and-his-shots/problem?isFullScreen=false

from bisect import bisect_left, bisect_right
from sys import stdin, stdout


class _Node:
    def __init__(self, center, by_low, by_high, left, right):
        self.center = center
        self.by_low = by_low
        self.by_high = by_high
        self.left = left
        self.right = right


def interval_tree(intervals):
    if intervals == []:
        return None
    center = intervals[len(intervals) // 2][0]
    L = []
    R = []
    C = []
    for I in intervals:
        if I[1] <= center:
            L.append(I)
        elif center < I[0]:
            R.append(I)
        else:
            C.append(I)
    by_low = sorted((I[0], I) for I in C)
    by_high = sorted((I[1], I) for I in C)
    IL = interval_tree(L)
    IR = interval_tree(R)
    return _Node(center, by_low, by_high, IL, IR)


def intervals_containing(t, p):
    if t is None:
        return []

    retval = intervals_containing(t.left, p) + intervals_containing(t.right, p)
    if p < t.center:
        i = bisect_right(t.by_low, p, key=lambda t: t[0])
        for k in range(i):
            retval.append(t.by_low[k][1])
    else:
        i = bisect_left(t.by_high, p, key=lambda t: t[0])
        for k in range(i, len(t.by_high)):
            retval.append(t.by_high[k][1])
    return retval


if __name__ == "__main__":
    N, M = map(int, stdin.readline().strip().split())

    intervals = [
        tuple(map(int, stdin.readline().strip().split())) for _ in range(N)
    ]
    query_intervals = [
        tuple(map(int, stdin.readline().strip().split())) for _ in range(M)
    ]

    print(f"intervals = {intervals}")
    print(f"query_intervals = {query_intervals}")
