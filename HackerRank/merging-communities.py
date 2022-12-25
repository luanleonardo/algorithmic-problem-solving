# https://www.hackerrank.com/challenges/merging-communities

from sys import stdin, stdout


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.size[u] > self.size[v]:
            u, v = v, u
        self.parent[u] = v
        self.size[v] += self.size[u]


if __name__ == "__main__":
    n, n_qry = map(int, stdin.readline().strip().split())

    uf = UnionFind(n)
    for _ in range(n_qry):
        qry = list(stdin.readline().strip().split())
        u = int(qry[1])
        if qry[0] == "M":
            v = int(qry[2])
            uf.union(u, v)
        else:
            u = uf.find(u)
            stdout.write(f"{uf.size[u]}\n")
