n = int(input('Fibonacci till :'))
a,b = 1,1
for i in range(n-1):
	#a,b = b,a+b
	#vs
	#a = b
	#b = a+b
	a,b = b,a+b
	print (a)
