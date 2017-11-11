def translate(word):
	translation = []
	for x in word:
		if x not in 'AEIOUaeiou ':
			translation.append(x)
			translation.append('o')
			translation.append(x)
		else:
			translation.append(x)
	return translation
t =translate(input('Enter String to translate to Robbers language:\n'))
print(''.join(t))
