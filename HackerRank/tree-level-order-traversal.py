# https://www.hackerrank.com/challenges/tree-level-order-traversal

from collections import deque
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


def bfs(root):
    explored = set([id(root)])
    frontier = deque([root])
    result = [root.value]
    while frontier:
        node = frontier.pop()
        for child in [node.left, node.right]:
            if child is None or id(child) in explored:
                continue
            explored.add(id(child))
            frontier.appendleft(child)
            result.append(child.value)
    return result


def level_order(root):
    if root is None:
        return ""
    return " ".join(map(str, bfs(root)))


if __name__ == "__main__":
    n = int(stdin.readline().strip())
    values = map(int, stdin.readline().strip().split())
    tree = BST()
    for value in values:
        tree.insert(value)
    stdout.write(f"{level_order(tree.root)}\n")
