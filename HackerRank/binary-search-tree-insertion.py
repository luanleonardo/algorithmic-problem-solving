# https://www.hackerrank.com/challenges/binary-search-tree-insertion

from sys import stdin, stdout


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.data}"


class BST:
    def __init__(self):
        self.root = None

    def _insert_data(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                return
            self._insert_data(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
                return
            self._insert_data(node.right, data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self._insert_data(self.root, data)


def preOrder(node):
    if node is None:
        return
    stdout.write(f"{node.data} ")
    preOrder(node.left)
    preOrder(node.right)


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    values = map(int, stdin.readline().strip().split())
    bst = BST()
    for value in values:
        bst.insert(value)
    preOrder(bst.root)
