# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list


class DoublyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.data}"

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.data}"
        return f"{self.data} {self.next}"

    def _insertAtEnd(self, data):
        if self.next is None:
            newNode = DoublyLinkedListNode(data)
            newNode.prev = self
            self.next = newNode
            return
        self.next._insertAtEnd(data)

    def insertAtEnd(self, data):
        if self.data is None:
            self.data = data
            return
        self._insertAtEnd(data)


# def insertAtBeginning(head, data):
#     newNode = DoublyLinkedListNode(data)
#     if head.data is None:
#         return newNode
#     head.prev = newNode
#     newNode.next = head
#     return newNode


# def reverse(head):
#     reversedHead = DoublyLinkedListNode()
#     currentNode = head
#     while currentNode:
#         reversedHead = insertAtBeginning(reversedHead, currentNode.data)
#         currentNode = currentNode.next
#     return reversedHead


def reverse(head):
    prevNode, currentNode = None, head
    while currentNode:
        currentNode.next, prevNode, currentNode = (
            prevNode,
            currentNode,
            currentNode.next,
        )
    return prevNode


if __name__ == "__main__":
    head = DoublyLinkedListNode()
    head.insertAtEnd(1)
    head.insertAtEnd(2)
    head.insertAtEnd(3)
    head.insertAtEnd(4)

    print(head)
    reversedHead = reverse(head)
    print(reversedHead)
