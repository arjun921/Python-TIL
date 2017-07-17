N = int(input())
na = [input() for i in range(N)]
Q = int(input())
nq = []
for x in range(Q):
	nq.append(input().strip().split())

print(na)
for x in nq:
	a = x[0]
	b = x[1]
	print(x)
