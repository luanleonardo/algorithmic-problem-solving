# https://www.hackerrank.com/challenges/balanced-brackets/

from collections import deque
from sys import stdin, stdout

n = int(stdin.readline().rstrip())
b = {"}": "{", ")": "(", "]": "["}
for i in range(n):
    s = stdin.readline().rstrip()
    q = deque()
    result = "YES"
    for c in s:
        if c in b.values():
            q.append(c)
            continue

        if not q or q.pop() != b[c]:
            result = "NO"
            break
    if result == "YES" and q:
        result = "NO"
    stdout.write(f"{result}\n")
