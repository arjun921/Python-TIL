T = int(input())
a = []
for x in range(T):
	a.append(input().strip().split(' '))

for x in a:
	n = float(x[0])
	d = float(x[1])
	res = n/d
	st = str(res)
	print(st[int(x[2])])
	# try:
	# except Exception as e:
	# 	print("0")
