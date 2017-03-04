from itertools import permutations as pm
A = input().split(' ')
for x in list(pm(A[0],int(A[1]))):
	print(''.join(x))