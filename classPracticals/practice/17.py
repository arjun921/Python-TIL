def ActualChecker(s,n,lastHalf):
	firstHalf = s[:n]
	lastHalfReverse = lastHalf[::-1]
	b = False
	if firstHalf == lastHalfReverse:
		return True
	else:
		return False

def palChecker(s):
	#preprocessing begins
	filteredText = []
	for x in s:
		x = x.lower()
		if x not in "!@#$%^&*(){}|:<>? []\',./":
			if x not in " ":
				filteredText.append(x)
	s = "".join(filteredText)
	#preprocessing end
	n = len(filteredText)/2
	n = int(n)
	if len(filteredText)%2==0:
		lastHalf = s[n:]
		return(ActualChecker(s,n,lastHalf))
	else:
		lastHalf = s[n+1:]
		return(ActualChecker(s,n,lastHalf))

	

s=input("Enter Sentence to check if palindrome or not:\n")
print(palChecker(s))