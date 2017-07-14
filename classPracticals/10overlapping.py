def overlapping(lis1,lis2):
    test = False
    for i in lis1:
        if i in lis2:
            test = True
            break
        else:
            test = False

    return test




lis1 = []
n = int(input('Enter Number of elements in list:'))
for x in range(n):
    lis1.append(input('Enter Members of list:'))

print(lis1)
lis2 = []
n = int(input('Enter Number of elements in list:'))
for x in range(n):
    lis2.append(input('Enter Members of list:'))
print(lis2)

print(overlapping(lis1,lis2))
