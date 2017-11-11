# https://projecteuler.net/problem=2
a = []
i=temp=sum = 1
bp = int(input())
a.append(i)
while True:
	fi = i+temp
	if fi%2==0:
		sum += fi
	if fi>bp:
		break
	a.append(fi)
	i = temp
	temp = fi
print(a)
print(sum)
