file_open_prime = open('prime.txt','w')

def storePrime():
	primenums = int(input("Enter number for prime"))
	for num in range(1,primenums):
		prime = True
		for i in range (2,num):
			if num%i==0:
				prime = False
		if prime:
			#print(num)
			file_open_prime.write(str(num) + ", ")
	return

storePrime()
