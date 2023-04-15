# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.data} -> NULL"
        return f"{self.data} -> {self.next}"

    def insertAtEnd(self, data):
        if self.next is None:
            self.next = SinglyLinkedListNode(data)
            return
        self.next.insertAtEnd(data)


# O(m + n) time | O(1) space
def _mergeLists(head1, head2):
    if head1.next is None:
        head1.next = head2
        return head1

    prev = head1
    curr, currMax = (
        (head1.next, head2)
        if head1.next.data <= head2.data
        else (head2, head1.next)
    )
    prev.next = curr

    while True:
        prev = curr
        if curr.next is None:
            prev.next = currMax
            return head1
        if curr.next.data < currMax.data:
            curr = curr.next
        else:
            curr, currMax = currMax, curr.next
        prev.next = curr


def mergeLists(head1, head2):
    mergedListHead = (
        _mergeLists(head1, head2)
        if head1.data <= head2.data
        else _mergeLists(head2, head1)
    )
    return mergedListHead


if __name__ == "__main__":
    head1 = SinglyLinkedListNode(1)
    head1.insertAtEnd(3)
    head1.insertAtEnd(7)
    print(head1)

    head2 = SinglyLinkedListNode(3)
    head2.insertAtEnd(4)
    print(head2)

    print(mergeLists(head1, head2))
