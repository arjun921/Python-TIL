s = input() 
temp=[]
for x in s:
	if x==x.upper():
		x=x.lower()
		temp.append(x)
	elif x==x.lower():
		x=x.upper()
		temp.append(x)
	else:	
		temp.append(x)
print(''.join(temp))
