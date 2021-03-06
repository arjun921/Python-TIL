# https://www.algoexpert.io/questions/Longest%20Balanced%20Substring
def balanced(s):
    stack = []
    if len(s)%2==0:
        for char in s:
            if char == '(':
                stack.append(char)
            if char == ')' and len(stack)!=0:
                stack.pop()
            elif char == ')':
                return False
        return len(stack) == 0
    else:
        return False

def generate_substrings(s):
    for i,start in enumerate(s):
        for j,end in enumerate(s):
            if j>i:
                yield s[i:j+1]


def longestBalancedSubstring(string):
    max_len = 0
    for substring in generate_substrings(string):
        substring_len = len(substring)
        if balanced(substring):
            if substring_len>max_len:
                max_len = substring_len
    return max_len

out = longestBalancedSubstring(input())
print(out)