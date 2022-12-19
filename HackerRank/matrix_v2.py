# https://www.hackerrank.com/challenges/matrix/

from sys import stdin, stdout


class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        self.parents[u] = v


def minTime(roads, machines, num_cities):
    uf = UnionFind(num_cities)
    roads = sorted(roads)
    res = 0
    while roads:
        w, u, v = roads.pop()
        u = uf.find(u)
        v = uf.find(v)
        if u in machines and v in machines:
            res += w
        if u in machines:
            machines.add(v)
        if v in machines:
            machines.add(u)
        uf.union(u, v)
    return res


if __name__ == "__main__":

    num_cities, K = map(int, stdin.readline().strip().split())
    roads = set()
    machines = set()
    for _ in range(num_cities - 1):
        u, v, w = map(int, stdin.readline().strip().split())
        roads.add((w, u, v))
    for _ in range(K):
        u = int(stdin.readline().strip())
        machines.add(u)

    stdout.write(f"{minTime(roads, machines, num_cities)}\n")
