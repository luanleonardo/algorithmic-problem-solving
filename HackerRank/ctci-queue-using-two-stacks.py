# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

from sys import stdin, stdout


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def peek(self):
        if not self.out_stack:
            return self.in_stack[0]
        return self.out_stack[-1]

    def push(self, value):
        self.in_stack.append(value)

    def pop(self):
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()


if __name__ == "__main__":
    q = int(stdin.readline().rstrip())
    queue = MyQueue()
    for _ in range(q):
        values = list(map(int, stdin.readline().rstrip().split()))
        if values[0] == 1:
            queue.push(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            stdout.write(f"{queue.peek()}\n")
