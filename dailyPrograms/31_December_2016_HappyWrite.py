def is_happy_number():
	seen = set()
	a = []
	for n in range(1,100):
		status = True
		while status:
			digits = [int(c) for c in str(n)]
			n = sum(digit**2 for digit in digits)
			if n == 1:
				a.append(n)
				status = True
			elif n in seen:
				status = False
			seen.add(n)
	return a
print(is_happy_number())
