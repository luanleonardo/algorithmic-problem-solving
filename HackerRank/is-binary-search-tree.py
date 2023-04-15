# https://www.hackerrank.com/challenges/is-binary-search-tree/

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def _check_binary_search_tree(root, min, max):
    if root is None:
        return True
    if root.data <= min or max <= root.data:
        return False
    check_left_tree = _check_binary_search_tree(
        root.left, min=min, max=root.data
    )
    check_right_tree = _check_binary_search_tree(
        root.right, min=root.data, max=max
    )
    return check_left_tree and check_right_tree


def check_binary_search_tree_(root):
    return _check_binary_search_tree(root, min=float("-inf"), max=float("inf"))
