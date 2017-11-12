s = int(input())
a = []
for x in range(1,s+1):
	if s%x==0:
		a.append(x)
def is_prime(n):
	for i in range(3,n):
		if n%i==0:
			return False
	return True
p = []
for x in a:
	if is_prime(x):
		p.append(x)
print(max(p))
