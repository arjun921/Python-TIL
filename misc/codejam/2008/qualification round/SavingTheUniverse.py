def CentralQueryProcessingSystem(engines,queries):
	swap = 0
	notEqual = True
	while notEqual:
		q=0
		e=-1
		if queries[q]==engines[e]:
			swap+=1
			q+=1
			e-=1
		notEqual = False
	return swap

#number of cases
N = int(input())
for x in range(1,N+1):
	# Number of search engines
	S = int(input())
	engines = set()
	queries = []
	for y in range(0,S):
		engines.add(input())
	#number of queries
	Q = int(input())
	for z in range(0,Q):
		queries.append(input())
	# print('')
	# engines.sort()
	queries.sort(reverse=True)
	swap = CentralQueryProcessingSystem(engines,queries)
	
	print('\nCase #{}: {}'.format(x,swap))