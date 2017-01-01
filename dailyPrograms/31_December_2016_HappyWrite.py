def happy(n):
	past = set()
	while n!=1:
		n = sum(int(i)**2 for i in str(n))
		if n in past:
			return False
		past.add(n)
	return True

a = []
for x in range(1,100):
	if happy(x)[:8]:
		a.append(x)

#a = [x for x in range(500) if happy(x)[:8]]
print (a)
