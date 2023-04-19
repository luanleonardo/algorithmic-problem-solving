# https://www.hackerrank.com/challenges/primsmstsub/problem?isFullScreen=false


from collections import defaultdict
from heapq import heappop, heappush


def build_graph(edges):
    graph = defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = w
        graph[v][u] = w
    return graph


def prims(n, edges, start):
    graph = build_graph(edges)

    X = {start}
    T = set()
    H = []

    key = dict()
    winner = dict()
    for v in graph:
        if v == start:
            continue
        if v in graph[start]:
            key[v] = graph[start][v]
            winner[v] = (start, v)
        else:
            key[v] = float("inf")
            winner[v] = None
        heappush(H, (key[v], v))

    while len(X) != n:
        c, w = heappop(H)
        X.add(w)
        T.add(winner[w])
        for y in graph[w]:
            if y in X:
                continue
            if graph[w][y] < key[y]:
                key[y] = graph[w][y]
                winner[y] = (w, y)
                heappush(H, (key[y], y))

    return sum(graph[u][v] for u, v in T), T
