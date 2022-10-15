# https://www.hackerrank.com/challenges/luck-balance

from sys import stdin, stdout

n, k = map(int, stdin.readline().rstrip().split())
c = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

sc = sorted(c)
ci = [0, 0]
lb = 0
while sc:
    l, t = sc.pop()
    ci[t] += 1
    if t == 0 or ci[1] <= k:
        lb += l
    else:
        lb -= l

stdout.write(f"{lb}\n")
