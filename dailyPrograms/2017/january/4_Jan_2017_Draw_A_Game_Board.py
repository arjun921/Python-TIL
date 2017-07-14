def draw(n):
	for x in range(n):
		print(" --- "*n)
		print("|   |"*n)
		print(" --- "*n)
	return

def draw2():
	a = '---'.join('    ')
	b = '   '.join('||||')
	print('\n'.join((a, b, a, b, a, b, a)))


n = int(input('Enter Game Board Grid Size'))
#draw(n)
draw2()
