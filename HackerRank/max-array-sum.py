# https://www.hackerrank.com/challenges/max-array-sum

from sys import stdin, stdout


# O(n) time | O(1) space
def maxSubsetSum(arr):
    f = max(0, arr[0])
    c = max(f, arr[1])
    for v in arr[2:]:
        f, c = c, max(f + max(0, v), c)
    return c


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split()))
    stdout.write(f"{maxSubsetSum(arr)}\n")
