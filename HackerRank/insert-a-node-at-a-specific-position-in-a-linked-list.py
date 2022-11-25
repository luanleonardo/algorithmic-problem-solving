# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list


class SinglyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        if self.next is None:
            return f"{self.data}"
        return f"{self.data} {self.next}"

    def _insert(self, data):
        if self.next is None:
            self.next = SinglyLinkedListNode(data)
            return
        self.next._insert(data)

    def insert(self, data):
        if self.data is None:
            self.data = data
            return
        self._insert(data)


def insertNodeAtPosition(head, data, position):
    newNode = SinglyLinkedListNode(data)
    if position == 0:
        newNode.next = head
        return newNode
    currentNode = head
    for _ in range(position - 1):
        currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


if __name__ == "__main__":
    head = SinglyLinkedListNode()
    head.insert(16)
    head.insert(13)
    head.insert(7)
    print(insertNodeAtPosition(head, 1, 2))
