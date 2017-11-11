def reverse(s):
	rev = []
	for x in range(1,len(s)+1):
        	rev.append(s[-x])
	print (''.join(rev))
	return

reverse(input())
