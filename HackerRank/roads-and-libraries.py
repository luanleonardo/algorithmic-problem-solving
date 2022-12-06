# https://www.hackerrank.com/challenges/torque-and-development/


class UnionFind:
    def __init__(self, n) -> None:
        self.size = [None] + [1] * n
        self.parent = [None] + list(range(1, n + 1))

    def find(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] > self.size[q]:
            p, q = q, p
        self.parent[p] = q
        self.size[q] += self.size[p]


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib

    uf = UnionFind(n)
    for f, t in cities:
        uf.union(f, t)

    ump = [True] + [False] * n
    cost = 0
    for i in range(1, n + 1):
        p = uf.find(i)
        if ump[p]:
            continue
        cost += c_lib + (uf.size[p] - 1) * c_road
        ump[p] = True

    return cost
