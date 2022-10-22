# https://www.hackerrank.com/challenges/components-in-graph

from collections import defaultdict, deque
from sys import stdin, stdout


def connected_components(graph, n):
    ncc = 0
    ccs = defaultdict(set)
    unexplored = [True] * (n + 1)
    for i in range(1, n // 2 + 1):
        if unexplored[i]:
            ncc += 1
            q = deque()
            q.appendleft(i)
            while q:
                v = q.pop()
                ccs[ncc].add(v)
                for w in graph[v]:
                    if unexplored[w]:
                        unexplored[w] = False
                        q.appendleft(w)
    return ccs


if __name__ == "__main__":

    n = int(stdin.readline().rstrip())
    g = defaultdict(list)
    for _ in range(n):
        u, v = map(int, stdin.readline().rstrip().split())
        g[u].append(v)
        g[v].append(u)

    ccs = connected_components(g, 2 * n)
    smallest_sizes = float("inf")
    largest_sizes = float("-inf")
    for cc_id, cc in ccs.items():
        if len(cc) == 1:
            continue

        if len(cc) < smallest_sizes:
            smallest_sizes = len(cc)

        if largest_sizes < len(cc):
            largest_sizes = len(cc)

    stdout.write(f"{smallest_sizes} {largest_sizes}\n")
