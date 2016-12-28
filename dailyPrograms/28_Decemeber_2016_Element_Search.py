def infunc(numlist):
	listlen = int(input('Enter length of list'))
	print('Enter numbers in ascending form:')
	for i in range(listlen):
		numlist.append(int(input()))
	return numlist

def searchfunc(numlist):
	el = input('Enter Number to search:')
	#search = False
	address = 0
	for i in numlist:
		truth = el == i
		if truth:
			address = numlist.index(i)
			search = True
			break
		else:
			search = False
	return el,address,search
numlist = []	

numlist = infunc(numlist)

el,address,search = searchfunc(numlist)

if search:
	print('Element {} found at {}'.format(el,address))
else:
	print('Element not found')
