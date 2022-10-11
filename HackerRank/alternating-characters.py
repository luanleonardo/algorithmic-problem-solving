# https://www.hackerrank.com/challenges/alternating-characters/
from sys import stdin, stdout


def alternatingCharacters(s):
    n = len(s)
    if n == 1:
        return 0

    lv = alternatingCharacters(s[: n // 2])
    rv = alternatingCharacters(s[n // 2 :])

    if s[: n // 2][-1] == s[n // 2 :][0]:
        return lv + rv + 1

    return lv + rv


q = int(stdin.readline().rstrip())

for _ in range(q):
    s = stdin.readline().rstrip()
    stdout.write(f"{alternatingCharacters(s)}\n")
