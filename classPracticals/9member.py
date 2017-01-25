def is_member():
	lis = []
	n = int(input('Enter Number of members for club:'))
	for x in range(n):
		lis.append(input('Enter Member of list:'))

	print('Members of the club:')
	print(lis)


	if input('Enter Something to check if in club or not:\n') in lis:
		return ('True')
	else:
		return ('False')
print(is_member())
