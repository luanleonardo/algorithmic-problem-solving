from itertools import accumulate
from sys import stdin, stdout

N, M = list(map(int, stdin.readline().split()))
x = [0] * N

for _ in range(M):
    a, b, k = list(map(int, stdin.readline().split()))

    x[a - 1] += k
    if b < N:
        x[b] -= k
    print(x)

stdout.write(f"{max(accumulate(x))}\n")
