# https://www.hackerrank.com/challenges/alternating-characters/
from sys import stdin, stdout


def alternatingCharacters(s):
    n = len(s)
    if n == 1:
        return 0

    l = alternatingCharacters(s[: n // 2])
    r = alternatingCharacters(s[n // 2 :])

    if s[: n // 2][-1] == s[n // 2 :][0]:
        return l + r + 1

    return l + r


q = int(stdin.readline().rstrip())

for _ in range(q):
    s = stdin.readline().rstrip()
    stdout.write(f"{alternatingCharacters(s)}\n")
