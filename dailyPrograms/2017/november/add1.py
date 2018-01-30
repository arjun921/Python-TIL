s = [int(input("Enter Number")) for x in range(int(input("Enter Number of:")))]
a = ""
for x in s:
	a = a+str(x)
a = int(a)+1
s = []
for x in str(a):
	s.append(int(x))
print(s)
