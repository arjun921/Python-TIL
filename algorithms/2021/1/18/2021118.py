# https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring

def get_substrings(string):
	substrings = {}
	for i,x in enumerate(string):
		for j,y in enumerate(string):
			substring = string[i:j+1]
			sub_length = len(substring)
			if sub_length>0 and substring==substring[::-1]:
				if sub_length in substrings:
					substrings[sub_length] += [substring]
				else:
					substrings[sub_length] = [substring]
	return substrings

def longestPalindromicSubstring(string):
	if len(string)==1:
		return string
    substrings = get_substrings(string)	
	keys = list(substrings.keys())
	keys.sort()	
	return substrings[keys[-1]][0]
		
