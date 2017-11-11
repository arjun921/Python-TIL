from itertools import combinations
A = input().split(' ')
for b in range(1,int(A[1])+1):
	for x in list(combinations(A[0],b)):
		print(''.join(x))