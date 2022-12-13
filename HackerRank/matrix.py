# https://www.hackerrank.com/challenges/matrix/

import random
from sys import stdin, stdout


def Find(uf, u):
    if uf[u] != u:
        uf[u] = Find(uf, uf[u])
    return uf[u]


def minTime(roads, machines, num_cities):
    uf = list(range(num_cities))
    roads = sorted(roads)
    res = 0
    while roads:
        w, u, v = roads.pop()
        if Find(uf, u) in machines and Find(uf, v) in machines:
            res += w
            continue
        if random.randint(0, 1):
            if Find(uf, u) in machines:
                machines.add(Find(uf, v))
            uf[Find(uf, u)] = Find(uf, v)
        else:
            if Find(uf, v) in machines:
                machines.add(Find(uf, u))
            uf[Find(uf, v)] = Find(uf, u)
    return res


if __name__ == "__main__":

    num_cities, K = map(int, stdin.readline().strip().split())
    roads = set()
    machines = set()
    for _ in range(num_cities - 1):
        u, v, w = map(int, stdin.readline().strip().split())
        roads.add((w, u, v))
    for _ in range(K):
        u = int(stdin.readline().strip())
        machines.add(u)

    stdout.write(f"{minTime(roads, machines, num_cities)}\n")
