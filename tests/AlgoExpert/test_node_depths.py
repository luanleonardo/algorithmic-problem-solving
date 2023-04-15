import pytest

from AlgoExpert.node_depths import BinaryTree, nodeDepths


@pytest.fixture
def binary_tree():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    return root


def test_node_depths_sum(binary_tree):
    actual = nodeDepths(binary_tree)
    assert actual == 16
