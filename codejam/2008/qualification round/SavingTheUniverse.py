def CentralQueryProcessingSystem(engines,queries):
	swap = 0
	notEqual = True
	while notEqual:
		temp = 0
		for q in range(1,len(queries)):
			if queries[q]==engines[temp]:
				swap+=1
				temp+=1
		notEqual = False
	return swap

#number of cases
N = int(input())
for x in range(1,N+1):
	# Number of search engines
	S = int(input())
	engines = []
	for y in range(1,S+1):
		engines.append(input())
	#number of queries
	Q = int(input())
	queries = []
	for z in range(1,Q+1):
		queries.append(input())
	print('')
	swap = CentralQueryProcessingSystem(engines,queries)
	print('Case #{}: {}'.format(x,swap))