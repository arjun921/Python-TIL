s = input()
s = s.upper()
lens = len(s)
consonants = set()
vowels = set()
unique = []
substrings = []
stuart = []
kevin = []

"""Consonants in s to list"""
for x in s:
	if x not in 'AEIOU':
                consonants.add(x)
"""Vowels in s to set"""
for x in s:
	if x in 'AEIOU':
		vowels.add(x)

"""adds all possible substrings to substringlist"""
for b in range(0,lens):
	for i in range(1,lens+1):
		if s[b:i]!="":
			substrings.append(s[b:i])
for let in vowels:
	for words in substrings:
		if words.startswith(let):
			kevin.append(words)
for let in consonants:
	for words in substrings:
		if words.startswith(let):
			stuart.append(words)
if len(kevin)>len(stuart):
	print ('Kevin {}'.format(len(kevin)))
elif len(stuart)>len(kevin):
	print ('Stuart {}'.format(len(stuart)))
else:
	print ('Draw')
