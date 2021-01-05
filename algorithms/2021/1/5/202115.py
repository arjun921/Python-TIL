# https://www.algoexpert.io/questions/Move%20Element%20To%20End

def moveElementToEnd(array, toMove):
	response_array = []
	end = []
    for i, elem in enumerate(array):
		if elem == toMove:
			end.append(elem)
		else:
			response_array.append(elem)
	
	return response_array+end
			
