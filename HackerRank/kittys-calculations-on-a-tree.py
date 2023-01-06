# https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem

from collections import defaultdict, deque
from sys import stdin, stdout


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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


# O(n) time | O(n) space, n=len(tree)
def tree_adj_to_prec(tree, root=0):
    n = len(tree)
    frontier = deque([root])
    explored = set([root])
    dist = [0] * n
    prec = [0] * n
    while frontier:
        node = frontier.pop()
        for neighbor in tree[node]:
            if neighbor in explored:
                continue
            explored.add(neighbor)
            frontier.appendleft(neighbor)
            dist[neighbor] = dist[node] + 1
            prec[neighbor] = node
    return dist, prec


if __name__ == "__main__":
    n, q = map(int, stdin.readline().strip().split())

    tree = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, stdin.readline().strip().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    result = []
    for _ in range(q):
        total = 0
        k = int(stdin.readline().strip())
        P = {x - 1 for x in map(int, stdin.readline().strip().split())}
        if k == 1:
            result.append(total)
