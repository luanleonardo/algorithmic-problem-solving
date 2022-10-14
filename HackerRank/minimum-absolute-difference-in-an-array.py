# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

from sys import stdin, stdout

n = int(stdin.readline().rstrip())
array = list(map(int, stdin.readline().rstrip().split()))

sorted_array = sorted(array)
min_abs_diff = float("inf")
for i in range(n - 1):
    abs_diff = abs(sorted_array[i + 1] - sorted_array[i])
    if abs_diff < min_abs_diff:
        min_abs_diff = abs_diff

stdout.write(f"{min_abs_diff}\n")
