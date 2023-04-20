from collections import defaultdict


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


def build_graph(edges):
    graph = defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = w
        graph[v][u] = w
    return graph


def kruskal(graph):
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((graph[u][v], u, v))
    edges.sort()
    uf = UnionFind(len(graph))
    mst = []
    for w, u, v in edges:
        if uf.find(u) == uf.find(v):
            continue
        uf.union(u, v)
        mst.append((u, v))
    return sum(graph[u][v] for u, v in mst), mst
