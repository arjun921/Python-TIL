# https://www.algoexpert.io/questions/Find%20Successor

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def inorder_traverse(tree,array):
	if tree.left is not None:
		inorder_traverse(tree.left, array)
	array.append(tree.value)
	if tree.right is not None:
		inorder_traverse(tree.right, array)
	return array
		
	

def findSuccessor(tree, node):
    # Write your code here.
	try:
		val = int(str(node.value))
	except Exception as e:
		return None
	array = inorder_traverse(tree, [])
	node_index = array.index(int(val))+1
	if val in array and node_index<len(array):
		return BinaryTree(array[node_index])
	else:
		return None