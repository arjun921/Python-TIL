s = input()
s = s.upper()
lens = len(s)
consonants = set()
vowels = set()
kevintot,stuarttot = 0,0

"""Consonants in s to list"""
for x in s:
	if x not in 'AEIOU':
		consonants.add(x)
"""Vowels in s to set"""
for x in s:
	if x in 'AEIOU':
		vowels.add(x)

"""adds all possible substrings to substringlist and counts scores without adding to newlist"""
for b in range(0,lens):
	for i in range(1,lens+1):
		if s[b:i]!="":
			ls = s[b:i]
			for let in vowels:
				if ls.startswith(let):
					kevintot += 1
			for let in consonants:
				if ls.startswith(let):
					stuarttot += 1

if kevintot>stuarttot:
	print ('Kevin {}'.format(kevintot))
elif stuarttot>kevintot:
	print ('Stuart {}'.format(stuarttot))
else:
	print ('Draw')
