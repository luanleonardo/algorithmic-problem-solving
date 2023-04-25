# https://www.hackerrank.com/challenges/tree-flow/problem?h_r=internal-search

from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin, stdout


def dijkstra(n_vertices, graph, start):
    seen = [False] * n_vertices
    seen[start] = True
    dist = [float("inf")] * n_vertices
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        dist_vertex, vertex = heappop(heap)
        for neighbor, weight in graph[vertex]:
            dist_neighbor = dist_vertex + weight
            if not seen[neighbor] and dist[neighbor] > dist_neighbor:
                seen[neighbor] = True
                dist[neighbor] = dist_neighbor
                heappush(heap, (dist_neighbor, neighbor))
    return dist


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    g = defaultdict(list)
    for _ in range(n - 1):
        u, v, w = map(int, stdin.readline().strip().split())
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    stdout.write(
        f"{min(sum(dijkstra(n_vertices=n, graph=g, start=0)),sum(dijkstra(n_vertices=n, graph=g, start=n - 1)))}\n"
    )
