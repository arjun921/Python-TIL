def is_member(s,ls):
	if s in ls:
		return True
	else:
		return False

ls = [1,2,4,6,7]
s = 9
print(is_member(s,ls))