t = int(input())
a = []
even=[]
odd=[]
for x in range(t):
	a.append(input())
	
for x in range(0,len(a)):
	temp = []
	for i in range(len(a[x])):
		if i%2==0:
			temp.append((a[x])[i])
	even.append("".join(temp))
	temp2 = []
	for i in range(len(a[x])):
		if i%2!=0:
			temp2.append((a[x])[i])
	odd.append("".join(temp2))
for s in zip(even,odd):
	print(s[0]+ " "+ s[1])
