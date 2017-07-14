def checkPrime():
	n = int(input("Enter number to check if prime or not"))
	b = n/2
	for i in range(2,int(b)):
		if n%i==0:
			return False
	return True

if checkPrime():
	print('Is prime')
else:
	print('Nop')
