# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree

from sys import stdin, stdout


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _insert_value(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_value(node.right, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._insert_value(self.root, value)

    def _height(self, node):
        if node is None or (node.left is None and node.right is None):
            return 0

        return max(self._height(node.left), self._height(node.right)) + 1

    def height(self):
        return self._height(self.root)


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    bst = BST()
    for v in map(int, stdin.readline().rstrip().split()):
        bst.insert(v)
    stdout.write(f"{bst.height()}\n")
