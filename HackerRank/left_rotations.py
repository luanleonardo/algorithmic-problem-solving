# https://www.hackerrank.com/challenges/array-left-rotation/

n, d = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
left_rotated_index = {(n - d + i) % n: i for i in range(n)}

print(" ".join([str(arr[left_rotated_index[i]]) for i in range(n)]))
