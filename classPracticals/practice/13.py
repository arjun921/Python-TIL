def max_in_list(ls):
	temp = ls[0]
	for x in ls:
		if x>temp:
			temp = x
	return temp
ls = [5,23,1,2,5,7,3]
print(max_in_list(ls))