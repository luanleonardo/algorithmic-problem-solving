# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/

from sys import stdin, stdout

t = int(stdin.readline().rstrip())
for _ in range(t):
    m = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    c = map(int, stdin.readline().rstrip().split())
    H = {}
    for i, v in enumerate(c):
        if m - v in H:
            stdout.write(f"{H[m - v] + 1} {i + 1}\n")
            break
        H[v] = i
