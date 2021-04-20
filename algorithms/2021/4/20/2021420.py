# https://www.algoexpert.io/questions/Invert%20Binary%20Tree

def invertBinaryTree(tree):
	if tree:
		tree.left, tree.right = tree.right, tree.left
		invertBinaryTree(tree.left)
		invertBinaryTree(tree.right)
	return tree
	


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
