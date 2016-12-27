import random,os
def game(cow,bull,rnum,unum):
	rnum = random.randint(1000,9999)
	#print (rnum)
	unum = int(input('Enter your guess:'))
	for i,j in zip(str(rnum),str(unum)):
		if i==j:
			cow = cow+1
		else:
			bull = bull+1
	print('Cows: {}'.format(cow))
	print('Bulls: {}'.format(bull))
	return cow,bull,rnum,unum

rnum,unum = 0,0
bull,cow = 0,0
condition = True
os.system('clr')
os.system('clear')
print('Lets Play a game of Cow Bull')
print('*'*90)
while(condition):
	cow,bull,rnum,unum = game(cow,bull,rnum,unum)
	if rnum==unum:
		condition = False
