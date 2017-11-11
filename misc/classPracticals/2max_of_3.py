def max_of_3(a,b,c):
	if a>b and a>c:
		return a
	elif b>a and b>c:
		return b
	elif c>a and c>b:
		return c

a = int(input('Enter Number A:'))
b = int(input('Enter Number B:'))
c = int(input('Enter Number C:'))
print(max_of_3(a,b,c))
