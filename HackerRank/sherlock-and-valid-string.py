# https://www.hackerrank.com/challenges/sherlock-and-valid-string/

from collections import Counter
from sys import stdin, stdout


def isValid(s):
    cl = Counter(s)
    cv = Counter(cl.values())

    if len(cv) == 1:
        return "YES"

    if len(cv) == 2:
        (fl1, nl1), (fl2, nl2) = cv.items()
        if (nl1 == 1 and (fl1 - 1 == fl2 or fl1 - 1 == 0)) or (
            nl2 == 1 and (fl2 - 1 == fl1 or fl2 - 1 == 0)
        ):
            return "YES"

    return "NO"


s = stdin.readline().rstrip()
result = isValid(s)
stdout.write(f"{result}\n")
