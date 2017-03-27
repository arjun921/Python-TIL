def translate(s):
	dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	translate = []
	for x in s:
		if x in dict:
			translate.append(dict[x])
	return translate

s = input().strip().split(' ')
print(s)
print (" ".join(translate(s)))