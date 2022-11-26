# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list


class DoublyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.data}"

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.data} {None}"
        return f"{self.data} {self.next}"

    def _insert(self, data):
        if self.next is None:
            newNode = DoublyLinkedListNode(data)
            newNode.prev = self
            self.next = newNode
            return
        self.next._insert(data)

    def insert(self, data):
        if self.data is None:
            self.data = data
            return
        self._insert(data)


def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)

    if data <= head.data:
        newNode.next = head
        head.prev = newNode
        return newNode

    currentNode = head.next
    while True:
        if data <= currentNode.data:
            currentNodePrev = currentNode.prev
            newNode.next = currentNode
            currentNode.prev = newNode
            currentNodePrev.next = newNode
            newNode.prev = currentNodePrev
            break
        if currentNode.next is None:
            newNode.prev = currentNode
            currentNode.next = newNode
            break
        currentNode = currentNode.next

    return head


if __name__ == "__main__":
    head = DoublyLinkedListNode()

    head.insert(1)
    head.insert(2)
    head.insert(4)

    print(sortedInsert(head, data=3))
