# https://www.algoexpert.io/questions/Validate%20Subsequence

def isValidSubsequence(array, sequence):
	last_array_index = 0
	if len(sequence)>len(array):
		return False
	if len(array)==len(sequence) and array!=sequence:
		return False
    for x in sequence:
		try:
			array_index = array.index(x)
			del array[array_index]
		except ValueError as e:
			return False
		if array_index>last_array_index:
			last_array_index = array_index
	return True
	
			
			
			
