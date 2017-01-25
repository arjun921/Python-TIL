def VowOrNot(c):
	c = c.upper()
	if len(c)==1:
		if c in 'AEIOU':
			return True
		else:
			return False
	else:
		print('Input Only one character')

print(VowOrNot(input('Enter Single Letter Character')))
