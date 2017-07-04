def number_needed(a,b):
	count = 0
	lis  = []
	for x in a:
		b = b.replace(x,"")
	return b
a = input()
b = input()

print(number_needed(a,b))
