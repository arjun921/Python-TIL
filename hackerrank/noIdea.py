s = input().split(' ')
happiness = 0
_all = input().split(' ')
A = set(input().split(' '))
B = set(input().split(' '))
for x in A:
	if x in _all:
		happiness+=1
for x in B:
	if x in _all:
		happiness-=1

print (happiness)