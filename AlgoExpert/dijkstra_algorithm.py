# https://www.algoexpert.io/questions/dijkstra's-algorithm

from heapq import heappop, heappush


def build_directed_graph(edges):
    graph = {vertex: dict() for vertex in range(len(edges))}
    for vertex, neighbors in enumerate(edges):
        for neighbor, weight in neighbors:
            graph[vertex][neighbor] = weight
    return graph


def dijkstra(graph, start):
    processed = [False] * len(graph)
    distances = [float("inf") if vertex != start else 0 for vertex in graph]
    heap = [(distances[start], start)]
    while heap:
        dist_vertex, vertex = heappop(heap)
        if not processed[vertex]:
            processed[vertex] = True
            for neighbor in graph[vertex]:
                dist_neighbor = dist_vertex + graph[vertex][neighbor]
                if dist_neighbor < distances[neighbor]:
                    distances[neighbor] = dist_neighbor
                    heappush(heap, (distances[neighbor], neighbor))
    return distances


def dijkstrasAlgorithm(start, edges):
    graph = build_directed_graph(edges)
    distances = dijkstra(graph, start)
    return list(map(lambda x: -1 if x == float("inf") else x, distances))
