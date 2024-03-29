# https://www.algoexpert.io/questions/branch-sums


# def _inorder_branch_sums(node=None, branch_values=None, branch_values_sum=None):
#     if node is None:
#         return
#     if branch_values is None:
#         branch_values = []
#     if branch_values_sum is None:
#         branch_values_sum = []
#
#     branch_values.append(node.value)
#     _inorder_branch_sums(node.left, branch_values, branch_values_sum)
#     if node.left is None and node.right is None:
#         branch_values_sum.append(sum(branch_values))
#     _inorder_branch_sums(node.right, branch_values, branch_values_sum)
#     branch_values.pop()
#
#
# Solution 1
# # O(n) time | O(n) space, n = number of nodes
# def branchSums(root):
#     branch_values_sum = []
#     _inorder_branch_sums(node=root, branch_values_sum=branch_values_sum)
#     return branch_values_sum


def _preorder_branch_sums(node, running_sum, branch_values_sum):
    if node is None:
        return
    running_sum += node.value
    if node.left is None and node.right is None:
        branch_values_sum.append(running_sum)
    _preorder_branch_sums(node.left, running_sum, branch_values_sum)
    _preorder_branch_sums(node.right, running_sum, branch_values_sum)


# Solution 2
# O(n) time | O(n) space, n = number of nodes
def branchSums(root):
    branch_values_sum = []
    _preorder_branch_sums(
        node=root, running_sum=0, branch_values_sum=branch_values_sum
    )
    return branch_values_sum
