import pytest

from AlgoExpert.evaluate_expression_tree import BinaryTree, evaluateExpressionTree


@pytest.fixture
def tree_root():
    root = BinaryTree(-1)

    root.left = BinaryTree(-2)
    root.right = BinaryTree(-3)

    root.left.left = BinaryTree(-4)
    root.left.right = BinaryTree(2)
    root.right.left = BinaryTree(8)
    root.right.right = BinaryTree(3)

    root.left.left.left = BinaryTree(2)
    root.left.left.right = BinaryTree(3)

    return root


def test_evaluate_expression(tree_root):
    expected = 6
    actual = evaluateExpressionTree(tree_root)
    assert actual == expected
