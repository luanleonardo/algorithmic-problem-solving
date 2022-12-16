# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/
from sys import stdin, stdout

# O(n) time | O(1) space
def fibonacci(n):
    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    stdout.write(f"{fibonacci(n)}\n")
