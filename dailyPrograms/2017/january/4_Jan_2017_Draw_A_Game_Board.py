def draw(n):
	for x in range(n):
		print(" --- "*n)
		print("|   |"*n)
		print(" --- "*n)
	return

n = int(input('Enter Game Board Grid Size'))
draw(n)
