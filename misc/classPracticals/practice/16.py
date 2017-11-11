def filter_long_words(ls,n):
	longest = []
	for x in ls:
		if len(x)>n:
			longest.append(x)
	return longest

ls = ["asdasd","asdgasd","asdhgasdjahsdasd","asdasdasdas"]
n = int(input())
print(filter_long_words(ls,n))