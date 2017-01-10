import re
n=int(input())
s = input()
r = re.compile("^[a-z]*$")
if len(s) in range(1,1001):
	if len(s)<=n:
		if r.match(s):
			for x in s:
				
		else:
			print('Invalid Input')
