def is_palindrome():
	s = input()
	rev = []
	for x in range(1,len(s)+1):
		rev.append(s[-x])
	rev=(''.join(rev))
	if s==rev:
		return True
	else:
		return False

print(is_palindrome())
