def sum_(ls):
	val = 0
	for x in ls:
		val+=x
	return val
def mul_(ls):
	mulVal = 1
	for x in ls:
		mulVal*=x
	return mulVal

a = [1,1,1,1,1]

print(sum_(a))
print(mul_(a))