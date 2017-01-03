prime = []
happy = [] 

open_happy = open("happy.txt","r")
open_prime = open("prime.txt","r")


hline = open_happy.readline()
while hline:
	happy.append(hline)
	hline = open_happy.readline()

pline = open_prime.readline()
while pline:
	prime.append(pline)
	pline = open_prime.readline()
common = []

for elem in prime:
	if elem in happy:
		common.append(elem)
print (common)	
