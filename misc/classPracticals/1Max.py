def maxx(a,b):
	if a<b:
		return b
	elif b<a:
		return a
i = int(input())
j = int(input())

print(maxx(i,j))
