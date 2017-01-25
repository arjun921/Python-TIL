def sumOf(ls):
	su = 0
	for x in ls:
		su+=x
	return su

def mulOf(ls):
	mu = 1
	for x in ls:
		mu*=x
	return mu


print('Sum of 1 2 3 4 = '+str(sumOf([1,2,3,4])))
print('Mul of 1 2 3 4 = '+str(mulOf([1,2,3,4])))
