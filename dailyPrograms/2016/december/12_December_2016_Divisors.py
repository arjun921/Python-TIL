r = int(input("Enter number"))


listr = list(range(1,r+1))


divisors = []
for i in listr:
	if r % i == 0:
		divisors.append(i)


print(divisors)

