# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle

from sys import stdin, stdout


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        stdout.write(str(node.data))

        node = node.next

        if node:
            stdout.write(sep)


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# O(n) time | O(n) space
def has_cycle(head):
    explored = set()
    current_node = head
    while current_node:
        current_node_id = id(current_node)
        if current_node_id in explored:
            return 1
        explored.add(current_node_id)
        current_node = current_node.next
    return 0


if __name__ == "__main__":

    tests = int(stdin.readline().strip())

    for tests_itr in range(tests):
        index = int(stdin.readline().strip())

        llist_count = int(stdin.readline().strip())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(stdin.readline().strip())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        stdout.write(str(int(result)) + "\n")
