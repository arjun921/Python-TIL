def panChecker(s):
	s = s.lower()
	all = "qwertyuiopasdfghjklzxcvbnm"
	for x in all:
		if x not in s:
			return False
		else:
			return True
s = input()
print(panChecker(s))