# https://www.algoexpert.io/questions/node-depths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# def nodeDepthsSum(node, running_sum, total_sum):
#     if node is None:
#         return
#     total_sum.append(running_sum)
#     nodeDepthsSum(node.left, running_sum + 1, total_sum)
#     nodeDepthsSum(node.right, running_sum + 1, total_sum)
#
#
# O(n) time | O(n) space, n = number of nodes
# def nodeDepths(root):
#     total_sum = []
#     nodeDepthsSum(node=root, running_sum=0, total_sum=total_sum)
#     return sum(total_sum)


# O(n) time | O(h) space, n = number of nodes, h = tree height
def nodeDepths(node, depth=0):
    if node is None:
        return 0

    return (
        depth
        + nodeDepths(node=node.left, depth=depth + 1)
        + nodeDepths(node=node.right, depth=depth + 1)
    )
