import getpass,os

#clears screen before executing game
os.system('clr')
os.system('clear')

#game commmences
print("*"*90)
print ("Rock Paper Scissors Game")
print ("="*90)

def playGame():
	print ("Enter player names followed by inputs as" + "\n R for rock,\n P for paper,\n S for scissor")
	pNameA = input("Enter Player 1 Name: ")
	pNameB = input("Enter Player 2 Name: ")

	#takes input in hidden format
	userA = getpass.getpass('{} input: '.format(pNameA))
	userB = getpass.getpass('{} input: '.format(pNameB))
	os.system('clr')
	os.system('clear')
	#convert lower case to upper if entered
	userA = userA.upper()
	userB = userB.upper()

	#list for checking invalid inputs
	inputs = ["R","P","S"]

	#checks if inputs are valid
	if userA==userB:
		print("Match Draw")
	else:	
		if userA in inputs and userB in inputs:
			#game logic begins
			print("Results\n" + "="*90 + "\n{} Entered {}".format(pNameA,userA) + "\n{} Entered {}\n".format(pNameB,userB))
			if userA == "R":
				print("{} wins".format(pNameA) if userB=='S' else "{} Wins".format(pNameB))
			if userA == "P":
				print("{} Wins".format(pNameA) if userB=='R' else "{} Wins".format(pNameB))
			if userA == "S":
				print("{} Wins".format(pNameA) if userB=='P' else "{} Wins".format(pNameB))
		else:
			print ("Invalid inputs")
		return

playAgain = "Y"
yes = ["Y","y"]

while(playAgain in yes):
	playGame()
	playAgain = input("="*90+"\nWould you like to play again?\n Enter Y or N\n")
	os.system('clr')
	os.system('clear')
