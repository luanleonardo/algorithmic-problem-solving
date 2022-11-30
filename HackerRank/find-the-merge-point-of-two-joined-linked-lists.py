# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists


class SinglyLinkedListNode:
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
            self.next = SinglyLinkedListNode(data)
            return
        return self.next.insertAtEnd(data)


# O(m + n) time | O(1) space
def findMergeNode(head1, head2):
    currNode1, currNode2 = head1, head2
    cross1, cross2 = False, False

    while currNode1 and currNode2:

        if currNode1 == currNode2:
            return currNode1.data
        currNode1, currNode2 = currNode1.next, currNode2.next

        if currNode1 is None and not cross1:
            currNode1 = head2
            cross1 = True

        if currNode2 is None and not cross2:
            currNode2 = head1
            cross2 = True


if __name__ == "__main__":
    headOne = SinglyLinkedListNode(1)
    headOne.insertAtEnd(2)
    headOne.insertAtEnd(3)
    print(headOne)

    headTwo = SinglyLinkedListNode(1)
    headTwo.next = headOne.next
    print(headTwo)

    print(findMergeNode(headOne, headTwo))
