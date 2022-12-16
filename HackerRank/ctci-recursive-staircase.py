# https://www.hackerrank.com/challenges/ctci-recursive-staircase

from sys import stdin, stdout


# O(n) time | O(1) space
def stepPerms(n):
    if n < 3:
        return n
    elif n == 3:
        return n + 1

    a, b, c = 1, 2, 4
    for _ in range(4, n + 1):
        a, b, c = b, c, a + b + c

    return c


if __name__ == "__main__":
    s = int(stdin.readline().strip())
    for _ in range(s):
        n = int(stdin.readline().strip())
        stdout.write(f"{stepPerms(n) % 10000000007}\n")
