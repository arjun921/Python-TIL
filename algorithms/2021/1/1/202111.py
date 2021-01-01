# https://www.algoexpert.io/questions/BST%20Traversal

def inOrderTraverse(tree, array):
	if tree.left is not None:
		inOrderTraverse(tree.left,array)
	array.append(tree.value)
	if tree.right is not None:
		inOrderTraverse(tree.right,array)
	return array
		

def preOrderTraverse(tree, array):
	array.append(tree.value)
    if tree.left is not None:
		preOrderTraverse(tree.left,array)
	if tree.right is not None:
		preOrderTraverse(tree.right,array)
	return array


def postOrderTraverse(tree, array):
    if tree.left is not None:
		postOrderTraverse(tree.left,array)
	if tree.right is not None:
		postOrderTraverse(tree.right,array)
	array.append(tree.value)
	return array
