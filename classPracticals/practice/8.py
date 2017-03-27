def is_palindrome(s):
	if s==s[::-1]:
		return True
	else:
		return False
s ="radar"
print(is_palindrome(s))