# https://www.hackerrank.com/challenges/tree-inorder-traversal

from sys import stdin, stdout


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"


class BST:
    def __init__(self):
        self.root = None

    def _insert_value(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return
            self._insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                return
            self._insert_value(node.right, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._insert_value(self.root, value)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    stdout.write(f"{node.value} ")
    inorder(node.right)


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    values = map(int, stdin.readline().strip().split())
    tree = BST()
    for value in values:
        tree.insert(value)
    inorder(tree.root)
