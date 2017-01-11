t = int(input())
a = []
even=[]
odd=[]
allevs=[]
allodds=[]
for x in range(t):
	a.append(input())
allevs = []
for x in a:
	for i in range(len(x)):
		if i%2==0:
			even.append(x[i])
		else:
			odd.append(x[i])
	print (even)
	print (odd)
	allevs.append(even)
	allodds.append(odd)

