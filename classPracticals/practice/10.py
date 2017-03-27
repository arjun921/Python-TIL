def overlapping(ls1,ls2):
	for x in ls1:
		if x in ls2:
			return True
			break
	return False

ls1 = [1,2,4,5,6]
ls2 = [12,412,51,52,31,52134,7]
print(overlapping(ls1,ls2))