# https://www.algoexpert.io/questions/Largest%20Range

def largestRange(array):
    array.sort()
	original_start = array[0]
	start = array[0]
	range_candidates = []
	for i,end in enumerate(array):
		diff = end-start
		if diff==1:
			start=end
		elif diff>1:
			range_candidates.append([original_start,start])
			original_start = end
			start = end
	range_candidates.append([original_start,end])
	diff_ranges = [x[1]-x[0] for x in range_candidates]
	return range_candidates[diff_ranges.index(max(diff_ranges))]
