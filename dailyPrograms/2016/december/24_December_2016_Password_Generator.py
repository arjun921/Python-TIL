import random

#Gives random characters, numbers or special characters
def createPass():
	return random.choice('abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^\/<>,.?:;{}[]_+')

#Recalls createPass for length of password(n) times
def passlen(n):
	for x in range(n):
		pList.append(createPass())
	return pList
n = int(input('Enter password size'))

pList = []
passlen(n)
print("".join(pList))
