def max_of_three(a,b,c):
	if a>b and a>c:
		return a
	elif b>c and b>a:
		return b
	else:
		return c
print("Largest: "+str(max_of_three((int(input())),(int(input())),(int(input())))))