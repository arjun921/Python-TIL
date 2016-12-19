checkPrime():
	n = int(input("Enter number to check if prime or not"))
	flag = 0
	b = n/2
	for i in range(2,int(b)):
		if n%i==0:
                        flag = 1
                        break
        return flag;

checkPrime()
print("{} is prime".format(n) if flag == 0 else "Number is not prime")
