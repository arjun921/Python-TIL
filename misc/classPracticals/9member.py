def is_member():
	lis = []
	n = int(input('Enter Number of elements in list:'))
	for x in range(n):
		lis.append(input('Enter Members of list:'))

	print('Members of the club:')
	print(lis)


	if input('Enter Something to check if in club or not:\n') in lis:
		return ('True')
	else:
		return ('False')
print(is_member())
