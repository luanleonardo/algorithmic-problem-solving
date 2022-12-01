# https://www.hackerrank.com/challenges/ctci-linked-list-cycle


from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"{self.data}"

    def __str__(self):
        if self.next is None:
            return f"{self.data} -> {None}"
        return f"{self.data} -> {self.next}"

    def insertAtEnd(self, data):
        if self.next is None:
            self.next = Node(data)
            return
        return self.next.insertAtEnd(data)


# O(n) time | O(1) space
def has_cycle(head):
    frontier = deque([head])
    explored = set([head.data])
    while frontier:
        node = frontier.pop()
        if node.next is None:
            return False
        if node.next.data in explored:
            return True
        explored.add(node.next.data)
        frontier.append(node.next)


if __name__ == "__main__":
    head = Node(1)
    head.insertAtEnd(2)
    head.insertAtEnd(3)
    print(head)
    head.next.next.next = head.next
    print(has_cycle(head))
