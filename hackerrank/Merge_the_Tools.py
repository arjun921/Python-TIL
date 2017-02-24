def merge_the_tools(string,k):
	l = len(string)
	divs = int(l/k)
	temp = 0
	tstring = ""
	tset = set()
	arr = []
	narr = []
	for i in range(1,divs+1):
		tstring = string[temp:i*k]
		for x in tstring:
			if x not in narr:
				narr.append(x)
		arr.append(narr)
		narr=[]
		temp = i*k
	for y in arr:
		print ("".join(y))

if __name__ == "__main__":
	string, k = input(),int(input())
	merge_the_tools(string,k)
