def reads():
	s = input('Enter String:')
	return s

def strips(s):
	stripped = s.split()
	return stripped

def reverses(words):
	lenWords = len(words)
	first = 0
	while first < lenWords:
		words[first], words[lenWords-1] = words[lenWords-1], words[first]
		first = first + 1
		lenWords = lenWords - 1
	return(words)
s = reads()
words = strips(s)
print (" ".join(reverses(words)))

