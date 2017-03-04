from itertools import product
A = [int(x) for x in input().split(' ')]
B = [int(x) for x in input().split(' ')]
for x in (list(product(A,B))):
	print (x, end="")