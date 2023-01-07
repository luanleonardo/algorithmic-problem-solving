# https://www.hackerrank.com/challenges/tree-top-view

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


# https://www.techiedelight.com/print-top-view-binary-tree/
def printTop(root, dist, level, d):
    if root is None:
        return
    if dist not in d or level < d[dist][1]:
        d[dist] = (root.value, level)
    printTop(root.left, dist - 1, level + 1, d)
    printTop(root.right, dist + 1, level + 1, d)


def printTopView(root):
    d = {}
    printTop(root, 0, 0, d)
    for key in sorted(d.keys()):
        print(d.get(key)[0], end=" ")


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    values = map(int, stdin.readline().strip().split())
    bst = BST()
    for value in values:
        bst.insert(value)
    printTopView(bst.root)
