# https://www.algoexpert.io/questions/Longest%20Balanced%20Substring
def balanced(string):
    stack = []
    if len(string)%2==0:
        for char in string:
            if char == '(':
                stack.append(char)
            if char == ')' and len(stack)!=0:
                stack.pop()
            elif char == ')':
                return False
        return len(stack) == 0
    else:
        return False

def generate_substrings(string):
	for i,start in enumerate(string):
        for j,end in enumerate(string):
            if j>i:
                yield string[i:j+1]

def update_max_len(max_len, new_value):
	if new_value>max_len:
		max_len = new_value

def longestBalancedSubstring(string):
	max_len = 0
    for substring in generate_substrings(string):
		substring_len = len(substring)
		if balanced(substring):
			if substring_len>max_len:
				max_len = substring_len
	return max_len