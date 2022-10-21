# https://www.hackerrank.com/challenges/angry-children/

from sys import stdin, stdout

n = int(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())

array = []
for _ in range(n):
    array.append(int(stdin.readline().rstrip()))
array.sort()

min_unfairness = float("inf")
for i in range(n - k + 1):
    unfairness = array[i + k - 1] - array[i]
    if unfairness < min_unfairness:
        min_unfairness = unfairness

stdout.write(f"{min_unfairness}\n")
