def draw(n):
	for x in range(n):
		printin(n)
		#for y in range(n):
		#	print("\t")
	return

def printin(n):
	print("\r",end="")
	print(" "+"-"*3)
	print("|"+" "*3+"|")
	print(" "+"-"*3)
	return

n = int(input('Enter Game Board Grid Size'))
draw(n)
