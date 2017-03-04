for i in range(1,int(input())+1):
	print (''.join([str(j) for j in range(1,i)]+[str(j) for j in range(i,0,-1)]))