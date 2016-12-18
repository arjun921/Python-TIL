import random
a = random.sample(range(100), 5)
b = random.sample(range(100), 9)

print (a)
print(b)

new = []
for i in a:
	if i in b:
		new.append(i)
new = set(new)
print (new)
