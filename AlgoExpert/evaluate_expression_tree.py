# https://www.algoexpert.io/questions/evaluate-expression-tree


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, n = number of nodes, h = tree height
def evaluateExpressionTree(node):
    if node.value >= 0:
        return node.value

    left_result = evaluateExpressionTree(node.left)
    right_result = evaluateExpressionTree(node.right)

    if node.value == -1:
        return left_result + right_result
    elif node.value == -2:
        return left_result - right_result
    elif node.value == -3:
        return int(left_result / right_result)
    return left_result * right_result
