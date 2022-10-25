# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/

from collections import deque
from sys import stdin, stdout

t = int(stdin.readline().rstrip())
for _ in range(t):
    m = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    c = list(map(int, stdin.readline().rstrip().split()))
    H = set(c)
    ans = deque()
    for i, v in enumerate(c, start=1):
        if m - v in H:
            ans.append(i)
            if len(ans) == 2:
                if sum(c[i - 1] for i in ans) == m:
                    break
                ans.popleft()

    stdout.write(" ".join(map(str, sorted(ans))) + "\n")
