# https://www.hackerrank.com/challenges/greedy-florist/
# ref: https://youtu.be/WeREk39RI4U

from sys import stdin, stdout

n, k = map(int, stdin.readline().rstrip().split())
c = sorted(map(int, stdin.readline().rstrip().split()), reverse=True)

ans, t = 0, 1
while c:
    b, c = c[:k], c[k:]
    ans += t * sum(b)
    t += 1

stdout.write(f"{ans}\n")
