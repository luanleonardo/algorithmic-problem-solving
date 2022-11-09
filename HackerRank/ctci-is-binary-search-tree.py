# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree


def _checkBST(node, min_value, max_value):
    if node is None:
        return True

    if node.data <= min_value or node.data >= max_value:
        return False

    check_left_subtree = _checkBST(node.left, min_value, node.data)
    check_right_subtree = _checkBST(node.right, node.data, max_value)
    return check_left_subtree and check_right_subtree


def checkBST(root):
    return _checkBST(root, float("-inf"), float("inf"))
