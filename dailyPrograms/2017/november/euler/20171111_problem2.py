# https://projecteuler.net/problem=2
a = []
i = 1
temp = 1
a.append(i)
sum = 0
while i<=4000000:
	fi = i+temp
	if fi%2==0:
		sum += fi
	a.append(fi)
	i = temp
	temp = fi
print(sum)
