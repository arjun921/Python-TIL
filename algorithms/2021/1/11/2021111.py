# https://www.algoexpert.io/questions/Nth%20Fibonacci

def getNthFib(n,counter=0, n1=0, n2=1):
	response = n1
	if n<counter:
		return n1
	counter+=1
	nth_fib = n1+n2
	n1 = n2
	n2 = nth_fib
	if n>counter:
		response = getNthFib(n,counter, n1, n2)
	return response
	
    