# https://www.hackerrank.com/challenges/crush/

from math import ceil, log2
from sys import stdin, stdout


class SegmentTree:
    def __init__(self, arr, INF=float("-inf")):
        self.arr = arr
        self.n = len(arr)
        self.N = (2 << ceil(log2(n))) - 1
        self.INF = INF
        self.tree = [self.INF] * (self.N)
        self.lazy = [0] * (self.N)
        self._build(0, 0, self.n - 1)

    def _left(self, node):
        return (node << 1) + 1

    def _right(self, node):
        return (node << 1) + 2

    def _build(self, node, l, r):
        if l == r:
            self.tree[node] = self.arr[l]
            return
        mid = (l + r) // 2
        self._build(self._left(node), l, mid)
        self._build(self._right(node), mid + 1, r)
        self.tree[node] = max(
            self.tree[self._left(node)], self.tree[self._right(node)]
        )

    def _lazy_propagation(self, node, tl, tr):
        self.tree[node] += self.lazy[node]
        if tl != tr:
            self.lazy[self._left(node)] += self.lazy[node]
            self.lazy[self._right(node)] += self.lazy[node]
        self.lazy[node] = 0

    def _update(self, node, tl, tr, l, r, v):
        if tl > tr:
            return

        if self.lazy[node] != 0:
            self._lazy_propagation(node, tl, tr)

        if r < tl or l > tr:
            return

        if l <= tl and tr <= r:
            self.lazy[node] += v
            self._lazy_propagation(node, tl, tr)
            return

        mid = (tl + tr) // 2
        self._update(self._left(node), tl, mid, l, r, v)
        self._update(self._right(node), mid + 1, tr, l, r, v)
        self.tree[node] = max(
            self.tree[self._left(node)], self.tree[self._right(node)]
        )

    def update(self, l, r, v):
        return self._update(0, 0, self.n - 1, l, r, v)

    def _query(self, node, tl, tr, l, r):
        if tl > tr:
            return self.INF

        if self.lazy[node] != 0:
            self._lazy_propagation(node, tl, tr)

        if r < tl or l > tr:
            return self.INF

        if l <= tl and tr <= r:
            return self.tree[node]

        mid = (tl + tr) // 2
        return max(
            self._query(self._left(node), tl, mid, l, r),
            self._query(self._right(node), mid + 1, tr, l, r),
        )

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)


def arrayManipulation(n, queries):
    st = SegmentTree(arr=[0] * n)
    for a, b, k in queries:
        st.update(a - 1, b - 1, k)
    return st.query(0, n - 1)


if __name__ == "__main__":

    n, m = tuple(map(int, stdin.readline().strip().split(" ")))

    queries = [
        tuple(map(int, stdin.readline().strip().split(" "))) for _ in range(m)
    ]

    result = arrayManipulation(n, queries)

    stdout.write(f"{result}\n")
