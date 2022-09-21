# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

from sys import stdin, stdout

n, d = tuple(map(int, stdin.readline().rstrip().split()))
arr = list(map(int, stdin.readline().rstrip().split()))
id_map = {(n - d + i) % n: i for i in range(n)}

stdout.write(" ".join([str(arr[id_map[i]]) for i in range(n)]) + "\n")
