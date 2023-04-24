# https://www.hackerrank.com/challenges/dijkstrashortreach/problem?isFullScreen=false

from heapq import heappop, heappush
# from sys import stdin, stdout


def dijkstra(graph, start):
    processed = [False] * len(graph)
    distances = [float("inf") if node != start else 0 for node in graph]
    heap = [(distances[start], start)]
    while heap:
        dist_node, node = heappop(heap)
        if not processed[node]:
            processed[node] = True
            for neighbor in graph[node]:
                dist_neighbor = dist_node + graph[node][neighbor]
                if dist_neighbor < distances[neighbor]:
                    distances[neighbor] = dist_neighbor
                    heappush(heap, (distances[neighbor], neighbor))
    return distances


# if __name__ == "__main__":
#     t = int(stdin.readline().strip())
#     for i in range(t):
#         n, m = map(int, stdin.readline().strip().split())
#         g = {u: dict() for u in range(n)}
#         for _ in range(m):
#             u, v, w = map(int, stdin.readline().strip().split())
#             u, v = u - 1, v - 1
#             if v in g[u] or u in g[v]:
#                 g[u][v] = min(g[u][v], w)
#                 g[v][u] = min(g[v][u], w)
#             else:
#                 g[u][v] = w
#                 g[v][u] = w
#         s = int(stdin.readline().strip()) - 1
#         answer = ""
#         for distance in dijkstra(graph=g, start=s):
#             if distance == 0:
#                 continue
#             if distance == float("inf"):
#                 answer += "-1 "
#             else:
#                 answer += f"{distance} "
#         answer.strip()
#         stdout.write(answer + "\n")
