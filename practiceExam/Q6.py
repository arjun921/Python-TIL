from math import sqrt
C = 50.0
H = 30.0
def calcQ(C,D,H):
	H = float(H)
	C = float(C)
	D = float(D)
	q =  sqrt(float(((2.00*C*D)/H)))
	q=round(q)
	return q

ls = input().strip().split(',')
output = []
for x in ls:
	output.append(str(calcQ(C,x,H)))
print(','.join(output))
#print(calcQ(C,(input().strip().split(',')),H))
