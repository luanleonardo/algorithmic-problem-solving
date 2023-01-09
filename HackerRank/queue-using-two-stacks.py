# https://www.hackerrank.com/challenges/queue-using-two-stacks

from sys import stdin, stdout


class Queue:
    def __init__(self):
        self.tail = []
        self.head = []

    def front(self):
        if not self.head:
            return self.tail[0]
        return self.head[-1]

    def enqueue(self, value):
        self.tail.append(value)

    def dequeue(self):
        if not self.head:
            self.head = self.tail[::-1]
            self.tail = []
        return self.head.pop()


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    queue = Queue()
    for _ in range(n):
        query = list(map(int, stdin.readline().strip().split()))
        type = query[0]
        if type == 1:
            queue.enqueue(query[1])
        elif type == 2:
            queue.dequeue()
        else:
            stdout.write(f"{queue.front()}\n")
