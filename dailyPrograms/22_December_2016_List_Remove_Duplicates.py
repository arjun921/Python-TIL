def readList():
	a = []
	n = int(input('Enter List size'))
	for x in range(1, n+1):
		a.append(input('Enter Element:'))
	return a

def retSet(newA):
	return set(newA)

newA = readList()
print (retSet(newA))
