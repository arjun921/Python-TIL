# https://www.algoexpert.io/questions/Binary%20Search

def binarySearch(array, target):
	start = 0
	end = len(array)-1
	while start<=end:
		middle = (start+end) // 2
		potential_match = array[middle]
		if target==potential_match:
			return middle
		elif target<potential_match:
			end = middle - 1
		else:
			start = middle + 1
	return -1