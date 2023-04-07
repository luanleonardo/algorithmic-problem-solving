# https://www.algoexpert.io/questions/find-closest-value-in-bst


# O(log N) time | O(1) space, N = number of nodes
def findClosestValueInBst(tree, target):
    node = tree
    closest_value = tree.value
    while True:
        if node is None or closest_value == target:
            return closest_value
        if abs(target - node.value) < abs(target - closest_value):
            closest_value = node.value
        node = node.right if node.value < target else node.left


# # O(log N) time | O(log N) space, N = number of nodes
# def _find_closest_value_in_bst(node, closest_value, target):
#     if node is None or closest_value == target:
#         return closest_value
#
#     if abs(target - node.value) < abs(target - closest_value):
#         closest_value = node.value
#
#     if node.value < target:
#         return _find_closest_value_in_bst(node.right, closest_value, target)
#     else:
#         return _find_closest_value_in_bst(node.left, closest_value, target)
#
#
# def findClosestValueInBst(tree, target):
#     return _find_closest_value_in_bst(tree, tree.value, target)
