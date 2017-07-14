s = input()
new = []
for x in s:
	if x.upper() not in 'AEIOU ':
		new.append(x)
		new.append('o')
		new.append(x)
	else:
		new.append(x)

print(''.join(new))