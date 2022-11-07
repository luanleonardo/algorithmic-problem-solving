def preOrderTraversal(array, tree):
    if not array:
        return
    mid = (len(array) - 1) // 2
    tree.insert(array[mid])
    preOrderTraversal(array[:mid], tree)
    preOrderTraversal(array[mid + 1 :], tree)


def minHeightBst(array):
    tree = BST()
    preOrderTraversal(array=array, tree=tree)
    return tree


class BST:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
