def vowOrNot(c):
	c=c.upper()
	if c in "AEIOU":
		return True
	else:
		return False
c = input('Enter Character:')
print(vowOrNot(c))