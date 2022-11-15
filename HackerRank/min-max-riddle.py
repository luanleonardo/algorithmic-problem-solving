# https://www.hackerrank.com/challenges/min-max-riddle

from collections import deque
from sys import stdin, stdout


# O(n^2) time | O(n) space
def riddle(arr):
    answer = []
    stack = deque(arr)
    while len(stack) > 1:
        max_window = stack[0]
        for i in range(len(stack) - 1):
            max_window = max(max_window, stack[i + 1])
            stack[i] = min(stack[i], stack[i + 1])
        stack.pop()
        answer.append(max_window)
    answer.append(stack.pop())
    return answer


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split()))
    stdout.write(" ".join(map(str, riddle(arr))) + "\n")
