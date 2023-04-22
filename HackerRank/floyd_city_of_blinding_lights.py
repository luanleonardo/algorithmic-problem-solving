# https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem?isFullScreen=false

# from sys import stdin, stdout


def build_distance_matrix(num_vertices, edges):
    vertices = range(num_vertices)
    matrix = [
        [float("inf") if i != j else 0 for j in vertices] for i in vertices
    ]
    for u, v, w in edges:
        matrix[u][v] = w
    return matrix


def floyd_warshall(distance_matrix):
    vertices = range(len(distance_matrix))
    for k in vertices:
        for u in vertices:
            for v in vertices:
                distance_matrix[u][v] = min(
                    distance_matrix[u][v],
                    distance_matrix[u][k] + distance_matrix[k][v],
                )


# if __name__ == "__main__":
#     n, m = map(int, stdin.readline().strip().split())
#     weighted_edges = []
#     for _ in range(m):
#         u, v, w = map(int, stdin.readline().strip().split())
#         weighted_edges.append((u - 1, v - 1, w))
#
#     distance_matrix = build_distance_matrix(
#         num_vertices=n, edges=weighted_edges
#     )
#     floyd_warshall(distance_matrix)
#
#     q = int(stdin.readline().strip())
#     for _ in range(q):
#         u, v = map(int, stdin.readline().strip().split())
#         if distance_matrix[u - 1][v - 1] == float("inf"):
#             stdout.write("-1\n")
#         else:
#             stdout.write(f"{distance_matrix[u - 1][v - 1]}\n")
