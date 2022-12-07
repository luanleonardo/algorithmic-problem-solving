# https://www.hackerrank.com/challenges/find-the-nearest-clone

from collections import defaultdict
from heapq import heappop, heappush
from itertools import combinations
from sys import stdin, stdout


def dijkstra(graph, source, sink):
    """
    implement Dijkstra algorithm on the graph to find the shortest path
    :param graph: a python dictionary representing the graph structure
    :param source: starting vertex
    :param sink: end vertex
    :return: shortest length, path from source to sink
    """
    queue = [(0, source, ())]
    visited = set()
    mins = {source: 0}
    while queue:
        (cost, vertex, path) = heappop(queue)
        if vertex in visited:
            continue

        visited.add(vertex)
        path += (vertex,)
        if vertex == sink:
            return cost, path

        for head, edge_cost in graph.get(vertex, ()):
            curr_cost = mins.get(head, None)
            new_cost = cost + edge_cost
            if curr_cost is None or new_cost < curr_cost:
                mins[head] = new_cost
                heappush(queue, (new_cost, head, path))

    return float("inf"), None


def findShortest(graph, node_color, node_by_color, color):
    if len(node_by_color[color]) < 2:
        return -1

    shortest_distance = float("inf")
    for u, v in combinations(node_by_color[color], 2):
        dist = dijkstra(graph, u, v)[0]
        if dist < shortest_distance:
            shortest_distance = dist

    return shortest_distance


if __name__ == "__main__":
    n, m = map(int, stdin.readline().rstrip().split())

    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, stdin.readline().rstrip().split())
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    node_color = [None] + list(map(int, stdin.readline().rstrip().split()))
    node_by_color = defaultdict(list)
    for node, color in enumerate(node_color):
        node_by_color[color].append(node)

    color = int(stdin.readline().rstrip())
    stdout.write(f"{findShortest(graph, node_color, node_by_color, color)}\n")
