# https://www.hackerrank.com/challenges/ctci-big-o

from math import sqrt
from sys import stdin, stdout

# O(sqrt(n)) time | O(1) space
def primality(n):
    if n == 1:
        return "Not prime"

    if n == 2:
        return "Prime"

    k = int(sqrt(n))
    for d in range(2, k + 1):
        if n % d == 0:
            return "Not prime"

    return "Prime"


if __name__ == "__main__":
    p = int(stdin.readline().strip())
    for _ in range(p):
        n = int(stdin.readline().strip())
        stdout.write(f"{primality(n)}\n")
