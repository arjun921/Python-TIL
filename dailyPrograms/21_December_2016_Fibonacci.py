n = int(input('Fibonacci till :'))

i = 0
j = 1
temp = 0
#print(i)
#print(j)
for i in range(1,n):
	temp = i + j
	i = j
	j = temp
	print (temp)
