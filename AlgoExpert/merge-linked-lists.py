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
            return f"{self.value}"
        return f"{self.value} -> {self.next}"

    def insertAtEnd(self, value):
        if self.next is None:
            self.next = LinkedList(value)
            return
        return self.next.insertAtEnd(value)


def _mergeLinkedLists(headOne, headTwo):
    if headOne.next is None:
        headOne.next = headTwo
        return headOne

    prev = headOne
    curr = headOne.next if headOne.next.value <= headTwo.value else headTwo
    currMax = headTwo if headOne.next.value <= headTwo.value else headOne.next
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
    headOne = LinkedList(2)
    headOne.insertAtEnd(6)
    headOne.insertAtEnd(7)
    headOne.insertAtEnd(8)
    print(headOne)

    headTwo = LinkedList(1)
    headTwo.insertAtEnd(3)
    headTwo.insertAtEnd(4)
    headTwo.insertAtEnd(5)
    headTwo.insertAtEnd(9)
    headTwo.insertAtEnd(10)
    print(headTwo)

    print(mergeLinkedLists(headTwo, headOne))
