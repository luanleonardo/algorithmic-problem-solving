# https://www.hackerrank.com/challenges/pairs

from sys import stdin, stdout

n, k = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))

H = set(arr)
ans = 0
for e in arr:
    if e - k in H:
        ans += 1
stdout.write(f"{ans}\n")
