def find_longest_word(ls):
	temp = ls[0]
	for x in ls:
		if len(x)>len(temp):
			temp = x
	return temp
ls = ["sadasdasda","asdasdasdasdasdasd","asdasdasduhgasjdhabsdjhagdja"]
print(find_longest_word(ls))