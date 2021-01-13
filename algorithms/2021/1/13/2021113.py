# https://www.algoexpert.io/questions/Right%20Smaller%20Than

def rightSmallerThan(array):
	response = [0 for x in array]
    for i,x in enumerate(array):
		for y in array[i:]:
			if y<x:
				response[i]+=1
	return response
