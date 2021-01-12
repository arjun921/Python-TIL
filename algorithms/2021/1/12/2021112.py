# https://www.algoexpert.io/questions/Shorten%20Path

def shortenPath(path):
	stack = []
	if path[0] =='/':
		stack.append('')
	path = [x for x in path.split('/') if len(x)>0 and x!='.']
	print(path)
	for x in path:
		if x == '..':
			if len(stack)==0 or stack[-1]=='..':
				stack.append(x)
			elif stack[-1]!='':
				stack.pop()
		else:
			stack.append(x)
	if len(stack)==1 and stack[0]=="":
		return "/"	
	return '/'.join(stack)