# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
from collections import deque
from sys import stdin, stdout


class Graph:
    def __init__(self, n):
        self.n = n
        self.neighbors = [[] for _ in range(self.n)]
        self.weight = [{} for _ in range(self.n)]

    def __getitem__(self, u):
        return self.neighbors[u]

    def connect(self, u, v, w=6):
        self.neighbors[u].append(v)
        self.neighbors[v].append(u)
        self.weight[u][v] = w
        self.weight[v][u] = w

    def bfs(self, s):
        frontier = deque([s])
        explored = set([s])
        dist = [-1] * self.n
        dist[s] = 0
        while frontier:
            node = frontier.pop()
            for neighbor in self[node]:
                if neighbor in explored:
                    continue
                explored.add(neighbor)
                frontier.appendleft(neighbor)
                dist[neighbor] = dist[node] + self.weight[node][neighbor]
        return dist

    def find_all_distances(self, s):
        dist = list(filter(lambda x: x != 0, self.bfs(s)))
        output = " ".join(map(str, dist))
        stdout.write(f"{output}\n")


if __name__ == "__main__":
    t = int(stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, stdin.readline().rstrip().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, stdin.readline().rstrip().split())
            graph.connect(u - 1, v - 1)
        s = int(stdin.readline().rstrip())
        graph.find_all_distances(s - 1)
