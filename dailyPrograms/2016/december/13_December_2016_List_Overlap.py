a = [1,2,3,6,2,5,7,9,2,3,7,9,10,25,89]
b = [1,2,6,8,3,1,7,0,00,335,247,21,681,146]

a = set (a)
b = set (b)

print(a)
print(b)


temp=[]
for numbers in a:
	if numbers in b:
		temp.append(numbers)

print(temp)

