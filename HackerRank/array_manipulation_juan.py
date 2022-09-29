# https://www.hackerrank.com/challenges/crush/

# Solução desenvolvida gentilmente por Juan Lopes (https://twitter.com/juanplopes)
from collections import Counter

n, m = map(int, input().split(" "))

T = Counter()
for _ in range(m):
    a, b, k = map(int, input().split(" "))
    T[a] += k
    T[b + 1] -= k

current, answer = 0, 0
for k, v in sorted(T.items()):
    current += v
    answer = max(answer, current)

print(answer)
