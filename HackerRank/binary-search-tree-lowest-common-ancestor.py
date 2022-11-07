# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor

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


if __name__ == "__main__":

    n = int(stdin.readline().rstrip())
    bst = BST()
    for v in map(int, stdin.readline().rstrip().split()):
        bst.insert(v)
    v1, v2 = sorted(map(int, stdin.readline().rstrip().split()))
    current_node = bst.root
    while True:
        if v1 <= current_node.value <= v2:
            lca = current_node.value
            break
        current_node = (
            current_node.right if current_node.value < v1 else current_node.left
        )
    stdout.write(f"{lca}\n")
