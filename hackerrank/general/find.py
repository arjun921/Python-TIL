def count_substring(string, sub_string):
	counter,count = 0,0
	for x in range(len(strng)):
		if string.find(sub_string)>=0:
			
	return counter

if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()
	count = count_substring(string, sub_string)
	print(count)
