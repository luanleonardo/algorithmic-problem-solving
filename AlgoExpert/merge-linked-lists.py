# https://www.algoexpert.io/questions/merge-linked-lists

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"{self.value}"

    def __str__(self):
        if self.next is None:
            return f"{self.value} -> NULL"
        return f"{self.value} -> {self.next}"

    def insertAtEnd(self, value):
        if self.next is None:
            self.next = LinkedList(value)
            return
        return self.next.insertAtEnd(value)


# O(m + n) time | O(1) space
def _mergeLinkedLists(headOne, headTwo):
    if headOne.next is None:
        headOne.next = headTwo
        return headOne

    prev = headOne
    curr, currMax = (
        (headOne.next, headTwo)
        if headOne.next.value <= headTwo.value
        else (headTwo, headOne.next)
    )
    prev.next = curr

    while True:
        prev = curr
        if curr.next is None:
            prev.next = currMax
            return headOne
        if curr.next.value < currMax.value:
            curr = curr.next
        else:
            curr, currMax = currMax, curr.next
        prev.next = curr


def mergeLinkedLists(headOne, headTwo):
    mergedHead = (
        _mergeLinkedLists(headOne, headTwo)
        if headOne.value <= headTwo.value
        else _mergeLinkedLists(headTwo, headOne)
    )
    return mergedHead


if __name__ == "__main__":
    headOne = LinkedList(1)
    headOne.insertAtEnd(3)
    headOne.insertAtEnd(7)
    print(headOne)

    headTwo = LinkedList(3)
    headTwo.insertAtEnd(4)
    print(headTwo)

    print(mergeLinkedLists(headOne, headTwo))
