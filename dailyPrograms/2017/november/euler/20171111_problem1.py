# https://projecteuler.net/problem=1
multips = []
for x in range(1,int(input())):
	if x%3==0 or x%5==0:
		multips.append(x)
print(sum(multips))
