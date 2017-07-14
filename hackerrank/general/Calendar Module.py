import calendar
def converter(i):	
	if i==0: s= "MONDAY"
	elif i==1: s="TUESDAY"
	elif i==2: s="WEDNESDAY"
	elif i==3: s="THURSDAY"
	elif i==4: s="FRIDAY"
	elif i==5: s="SATURDAY"
	elif i==6: s="SUNDAY"
	return s 
ins = input().strip().split(" ")
i = ((calendar.weekday(int(ins[2]), int(ins[0]), int(ins[1]))))
print(converter(i))
