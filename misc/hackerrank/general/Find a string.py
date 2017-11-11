def count_substring(string,sub_string):
	fl=True
	num=0	
	for i in range(len(string)):
		if string[i]==sub_string[0]:
			num=i
			break
	for i in range(num,len(sub_string)):
		for j in sub_string:
			if string[i]==j:
				fl+=True
			else:
				fl+=False
	if fl:
		return num

if __name__ == '__main__':
	string = input().strip()
	sub_string =  input().strip()
	count = count_substring(string,sub_string)
	print(count)
