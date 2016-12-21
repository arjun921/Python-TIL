def fibon(n):
	a,b = 1,1
	print (a)
	for i in range(n-1):
		#a,b = b,a+b
		#vs
		#a = b
		#b = a+b
		a,b = b,a+b
		print (a)

n = int(input('Fibonacci till :'))
fibon(n)
