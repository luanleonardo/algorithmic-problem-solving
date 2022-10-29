# https://www.hackerrank.com/challenges/swap-nodes-algo

from collections import deque
from sys import stdin, stdout


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def in_order_traversal(root):
    q = deque([root])
    visited = set()
    result = []
    while q:
        node = q.pop()
        if node is None:
            continue
        if node.value in visited:
            result.append(node.value)
            continue
        visited.add(node.value)
        q.append(node.right)
        q.append(node)
        q.append(node.left)
    return " ".join(map(str, result))


def swap_children(root, k):
    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        q.append((node.left, level + 1))
        q.append((node.right, level + 1))


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    tree = [None] + [Node(i) for i in range(1, n + 1)]
    for i in range(1, n + 1):
        a, b = map(int, stdin.readline().rstrip().split())
        if a > 0:
            tree[i].left = tree[a]
        if b > 0:
            tree[i].right = tree[b]
    t = int(stdin.readline().rstrip())
    root = tree[1]
    for _ in range(t):
        k = int(stdin.readline().rstrip())
        swap_children(root, k)
        stdout.write(f"{in_order_traversal(root)}\n")
