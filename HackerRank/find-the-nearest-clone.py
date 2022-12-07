# https://www.hackerrank.com/challenges/find-the-nearest-clone

from collections import defaultdict
from heapq import heappop, heappush
from itertools import combinations
from sys import stdin, stdout


def dijkstra(graph, source, destination):
    frontier = [(0, source, ())]
    explored = set()
    min_costs = {source: 0}
    while frontier:
        (cost, current_node, path) = heappop(frontier)
        if current_node in explored:
            continue

        explored.add(current_node)
        path += (current_node,)
        if current_node == destination:
            return cost, path

        for neighbor, edge_cost in graph.get(current_node, ()):
            current_cost = min_costs.get(neighbor, None)
            new_cost = cost + edge_cost
            if current_cost is None or new_cost < current_cost:
                min_costs[neighbor] = new_cost
                heappush(frontier, (new_cost, neighbor, path))

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
